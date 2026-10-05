import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/seam_color.py'
spec = importlib.util.spec_from_file_location('seam_color', SCRIPT)
seam = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seam)


class SeamColorTests(unittest.TestCase):
    def test_edges_preserve_interior_for_odd_rectangular_input(self):
        src = np.random.default_rng(7).integers(70, 180, (129, 161, 3), dtype=np.uint8)
        dst = seam.correct_edges(src)
        self.assertEqual(dst.shape, src.shape)
        self.assertEqual(seam.edge_metrics(dst)['lr_max'], 0)
        self.assertEqual(seam.edge_metrics(dst)['tb_max'], 0)
        np.testing.assert_array_equal(src[20:-20, 20:-20], dst[20:-20, 20:-20])

    def test_uniform_image_remains_identical(self):
        src = np.full((128, 128, 3), [110, 95, 82], np.uint8)
        np.testing.assert_array_equal(src, seam.correct_edges(src))

    def test_region_changes_only_selected_material(self):
        src = np.random.default_rng(9).integers(80, 170, (128, 128, 3), dtype=np.uint8)
        src = seam.equalize_endpoints(src)
        config = {'image_size': [128, 128], 'points': [[30,30],[97,30],[97,97],[30,97]],
                  'feather': 5, 'sigma': 3, 'core_distance': 8}
        dst, mask = seam.correct_region(src, config)
        np.testing.assert_array_equal(src[~mask], dst[~mask])
        self.assertTrue(np.any(src[mask] != dst[mask]))
        self.assertEqual(seam.edge_metrics(dst)['lr_max'], 0)
        self.assertEqual(seam.edge_metrics(dst)['tb_max'], 0)
        with self.assertRaises(ValueError):
            seam.correct_region(src, {**config, 'image_size': [256,256]})

    def test_cli_exports_and_refuses_overwrite_and_alpha(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            src, out = root/'source.png', root/'out.png'
            Image.new('RGB', (32, 32), (120, 95, 80)).save(src)
            argv = ['seam_color', str(src), str(out), '--mode', 'edges']
            with patch.object(sys, 'argv', argv):
                seam.main()
                original = out.read_bytes()
                with self.assertRaises(SystemExit):
                    seam.main()
                self.assertEqual(original, out.read_bytes())
            self.assertTrue(Path(str(out)+'.json').exists())
            self.assertTrue((root/'out-offset.png').exists())
            self.assertTrue((root/'out-2x2.jpg').exists())
            Image.new('RGBA', (32,32)).save(src)
            with patch.object(sys, 'argv', ['seam_color',str(src),str(root/'alpha.png'),'--mode','edges']):
                with self.assertRaises(SystemExit):
                    seam.main()
            self.assertFalse((root/'alpha.png').exists())


if __name__ == '__main__':
    unittest.main()
