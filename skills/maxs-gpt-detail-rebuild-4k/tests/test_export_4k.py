"""Run with: python -m unittest discover -s tests (from this skill folder)."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "export_4k.py"
SPEC = importlib.util.spec_from_file_location("export_4k", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_dimensions_transparency_and_honest_record(self):
        source = self.folder / "原始增强.png"
        output = self.folder / "四千.png"
        Image.new("RGBA", (80, 40), (10, 20, 30, 128)).save(source)
        original_bytes = source.read_bytes()
        report = MODULE.export_image(source, output)
        with Image.open(output) as image:
            self.assertEqual(image.size, (4096, 2048))
            self.assertEqual(image.mode, "RGBA")
            self.assertEqual(image.getpixel((2048, 1024))[3], 128)
        self.assertEqual(source.read_bytes(), original_bytes)
        self.assertFalse(report["ai_detail_reconstruction_performed_by_this_script"])
        self.assertEqual(report["source_size"], [80, 40])
        self.assertEqual(json.loads(output.with_suffix(".png.json").read_text()), report)

    def test_portrait_and_custom_long_edge(self):
        source = self.folder / "portrait.png"
        Image.new("RGB", (21, 40)).save(source)
        report = MODULE.export_image(source, self.folder / "result.png", 3840)
        self.assertEqual(report["output_size"], [2016, 3840])

    def test_same_size_does_not_resample(self):
        source = self.folder / "source.png"
        Image.new("RGB", (64, 32), (19, 42, 87)).save(source)
        output = self.folder / "result.png"
        report = MODULE.export_image(source, output, 64)
        self.assertEqual(report["resampling"], "none")
        with Image.open(source) as before, Image.open(output) as after:
            self.assertEqual(before.tobytes(), after.tobytes())

    def test_exif_rotation(self):
        source = self.folder / "rotated.jpg"
        orientation = Image.Exif()
        orientation[274] = 6
        Image.new("RGB", (80, 40)).save(source, exif=orientation)
        report = MODULE.export_image(source, self.folder / "result.png", 400)
        self.assertEqual(report["oriented_source_size"], [40, 80])
        self.assertEqual(report["output_size"], [200, 400])

    def test_existing_output_or_report_is_not_overwritten(self):
        source = self.folder / "source.png"
        Image.new("RGB", (10, 10)).save(source)
        output = self.folder / "result.png"
        output.write_bytes(b"keep image")
        with self.assertRaises(FileExistsError):
            MODULE.export_image(source, output)
        self.assertEqual(output.read_bytes(), b"keep image")
        other = self.folder / "other.png"
        other.with_suffix(".png.json").write_text("keep report")
        with self.assertRaises(FileExistsError):
            MODULE.export_image(source, other)
        self.assertFalse(other.exists())

    def test_invalid_requests(self):
        source = self.folder / "source.png"
        Image.new("RGB", (10, 10)).save(source)
        for output, edge in [(source, 4096), (self.folder / "a.jpg", 4096),
                             (self.folder / "b.png", 0)]:
            with self.subTest(output=output, edge=edge):
                with self.assertRaises(ValueError):
                    MODULE.export_image(source, output, edge)


if __name__ == "__main__":
    unittest.main()
