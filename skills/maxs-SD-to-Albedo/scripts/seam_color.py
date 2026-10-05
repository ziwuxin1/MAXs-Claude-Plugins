"""Local RGB8 albedo seam color correction, not geometry or PBR reconstruction."""
import argparse
import hashlib
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image


def edge_metrics(a):
    a = a.astype(np.float32)
    lr, tb = np.abs(a[:, 0] - a[:, -1]), np.abs(a[0] - a[-1])
    return {"lr_mean": float(lr.mean()), "tb_mean": float(tb.mean()),
            "lr_max": float(lr.max()), "tb_max": float(tb.max())}


def equalize_endpoints(a):
    a = a.copy()
    pair = np.round((a[:, 0].astype(np.float32) + a[:, -1]) / 2).astype(np.uint8)
    a[:, 0] = pair
    a[:, -1] = pair
    pair = np.round((a[0].astype(np.float32) + a[-1]) / 2).astype(np.uint8)
    a[0] = pair
    a[-1] = pair
    return a


def edge_field(length, width):
    d = np.minimum(np.arange(length), np.arange(length)[::-1]).astype(np.float32)
    t = np.clip(1 - d / width, 0, 1)
    w = t * t * (3 - 2 * t) * 0.5
    w[length // 2:] *= -1
    return w


def correct_edges(src):
    """Smooth additive boundary fields; preserve coordinates and interior pixels."""
    a = src.astype(np.float32)
    scale = min(a.shape[:2]) / 2048
    for sigma, width in [(24, 260), (8, 100), (2, 24), (0, 3)]:
        sigma, width = sigma * scale, max(1, width * scale)
        for axis in [1, 0]:
            low = cv2.GaussianBlur(a, (0, 0), sigma,
                                   borderType=cv2.BORDER_REFLECT_101) if sigma else a
            if axis == 1:
                delta = low[:, -1] - low[:, 0]
                a = a + delta[:, None] * edge_field(a.shape[1], width)[None, :, None]
            else:
                delta = low[-1] - low[0]
                a = a + delta[None] * edge_field(a.shape[0], width)[:, None, None]
    return equalize_endpoints(np.round(np.clip(a, 0, 255)).astype(np.uint8))


def correct_region(src, config):
    """Harmonize one selected material in half-offset view; no full-image redraw."""
    h, w = src.shape[:2]
    if config['image_size'] != [w, h]:
        raise ValueError('Region coordinates require the exact configured image_size.')
    if edge_metrics(src)['lr_max'] or edge_metrics(src)['tb_max']:
        raise ValueError('Region mode requires matched endpoints; use edges mode first.')
    points = np.asarray(config['points'], dtype=np.float64)
    if (points.ndim != 2 or points.shape[1] != 2 or len(points) < 3
            or not np.isfinite(points).all() or (points < 0).any()
            or (points[:, 0] >= w).any() or (points[:, 1] >= h).any()):
        raise ValueError('Use at least three finite, in-bounds polygon points.')
    feather = float(config.get('feather', 18))
    sigma = float(config.get('sigma', 6))
    core_distance = float(config.get('core_distance', 28))
    strength = np.array([config.get('luminance_strength', 0.65),
                         config.get('chroma_strength', 1.0),
                         config.get('chroma_strength', 1.0)], np.float32)
    if (not np.isfinite([feather, sigma, core_distance, *strength]).all()
            or min(feather, sigma, core_distance) <= 0
            or (strength < 0).any() or (strength > 1).any()):
        raise ValueError('Positive radii and strengths within [0, 1] are required.')
    shifted = np.roll(src, (h // 2, w // 2), (0, 1))
    mask = np.zeros((h, w), np.uint8)
    cv2.fillPoly(mask, [points.astype(np.int32)], 255)
    dist = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
    core = dist > core_distance
    if not core.any():
        raise ValueError('Polygon is too small for core_distance.')
    t = np.clip(dist / feather, 0, 1)
    weight = t * t * (3 - 2 * t)
    lab = cv2.cvtColor(shifted.astype(np.float32) / 255, cv2.COLOR_RGB2LAB)
    binary = (mask > 0).astype(np.float32)
    den = cv2.GaussianBlur(binary, (0, 0), sigma)
    low = cv2.GaussianBlur(lab * binary[:, :, None], (0, 0), sigma)
    low /= np.maximum(den[:, :, None], 1e-6)
    target = np.median(low[core], axis=0)
    edited = lab + (target - low) * strength * weight[:, :, None]
    rgb = np.round(np.clip(cv2.cvtColor(edited, cv2.COLOR_LAB2RGB), 0, 1) * 255).astype(np.uint8)
    rgb[mask == 0] = shifted[mask == 0]
    result = equalize_endpoints(np.roll(rgb, (-(h // 2), -(w // 2)), (0, 1)))
    selected = np.roll(mask > 0, (-(h // 2), -(w // 2)), (0, 1))
    if np.any(result[~selected] != src[~selected]):
        raise ValueError('Polygon must cover both sides of any edited periodic boundary.')
    return result, selected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--mode', choices=['edges', 'region'], required=True)
    parser.add_argument('--region', type=Path, help='JSON polygon in half-offset coordinates')
    args = parser.parse_args()
    output = args.output.resolve()
    paths = [output, Path(str(output) + '.json'),
             output.with_name(output.stem + '-offset.png'),
             output.with_name(output.stem + '-2x2.jpg')]
    if output.suffix.lower() != '.png':
        parser.error('Output must be PNG.')
    if output == args.source.resolve() or any(p.exists() for p in paths):
        parser.error('Refusing to overwrite source, output or validation sidecars.')
    if (args.mode == 'region') != bool(args.region):
        parser.error('--region is required only for region mode.')
    with Image.open(args.source) as im:
        if im.mode != 'RGB' or min(im.size) < 16:
            parser.error('This helper accepts RGB8 albedo at least 16x16 only; no alpha/data maps.')
        src = np.array(im)
    try:
        selected = None
        config = None
        if args.mode == 'edges':
            result = correct_edges(src)
        else:
            config = json.loads(args.region.read_text(encoding='utf-8'))
            result, selected = correct_region(src, config)
    except (ValueError, KeyError, TypeError) as exc:
        parser.error(str(exc))
    changed = np.any(src != result, axis=2)
    report = {'mode': args.mode, 'size': [src.shape[1], src.shape[0]],
              'source_sha256': hashlib.sha256(args.source.read_bytes()).hexdigest(),
              'before': edge_metrics(src), 'after': edge_metrics(result),
              'changed_pixels': int(changed.sum()), 'changed_fraction': float(changed.mean()),
              'region': config,
              'outside_region_unchanged': bool(not (changed & ~selected).any()) if selected is not None else None,
              'limitations': 'Color correction only. No coordinate resampling. Equal edge pixels do not prove visual seamlessness; inspect offset, 2x2 and junction at native scale. No AI detail reconstruction or engine validation.'}
    output.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(result).save(paths[0])
    paths[1].write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    Image.fromarray(np.roll(result, (len(result) // 2, result.shape[1] // 2), (0, 1))).save(paths[2])
    thumb = Image.fromarray(result)
    thumb.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
    preview = Image.new('RGB', (thumb.width * 2, thumb.height * 2))
    for y in range(2):
        for x in range(2):
            preview.paste(thumb, (x * thumb.width, y * thumb.height))
    preview.save(paths[3], quality=96)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
