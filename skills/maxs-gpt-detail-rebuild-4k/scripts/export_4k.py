#!/usr/bin/env python3
"""Export an already enhanced image at a target long edge; NOT an AI upscaler."""

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps


def export_image(source: Path, output: Path, long_edge: int = 4096) -> dict:
    source, output = Path(source).resolve(), Path(output).resolve()
    report_path = output.with_suffix(output.suffix + ".json")
    if long_edge < 1:
        raise ValueError("long_edge must be positive")
    if source == output:
        raise ValueError("Source and output must be different")
    if output.suffix.lower() != ".png":
        raise ValueError("Output must be a .png file")
    if output.exists() or report_path.exists():
        raise FileExistsError("Output or metadata exists; choose a new filename")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    with Image.open(source) as opened:
        if getattr(opened, "n_frames", 1) != 1:
            raise ValueError("Animated or multi-frame input is not supported")
        original_size = opened.size
        icc = opened.info.get("icc_profile")
        image = ImageOps.exif_transpose(opened)
        oriented_size = image.size
        has_alpha = "A" in image.getbands() or "transparency" in image.info
        image = image.convert("RGBA" if has_alpha else "RGB")
        scale = long_edge / max(image.size)
        target = tuple(max(1, round(size * scale)) for size in image.size)
        if image.size != target:
            image = image.resize(target, Image.Resampling.LANCZOS)
        output.parent.mkdir(parents=True, exist_ok=True)
        options = {"icc_profile": icc} if icc else {}
        # Exclusive creation prevents accidental overwrite even after preflight.
        with output.open("xb") as stream:
            image.save(stream, format="PNG", **options)
    with Image.open(output) as verified:
        verified.load()
        if verified.size != target:
            raise RuntimeError("Saved image dimensions do not match the target")
        output_mode = verified.mode
    report = {
        "operation": "size-export-only",
        "ai_detail_reconstruction_performed_by_this_script": False,
        "source_sha256": source_hash,
        "source_size": list(original_size),
        "oriented_source_size": list(oriented_size),
        "output_size": list(target),
        "target_long_edge": long_edge,
        "resampling": "Lanczos" if oriented_size != target else "none",
        "output_mode": output_mode,
        "note": "Any upstream AI reconstruction must be recorded separately.",
    }
    with report_path.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--long-edge", type=int, default=4096)
    args = parser.parse_args()
    try:
        report = export_image(args.source, args.output, args.long_edge)
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(1, f"Export failed: {exc}\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
