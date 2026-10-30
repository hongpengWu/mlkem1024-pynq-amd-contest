"""Read-only package validation; does not launch EDA or access a board."""
import ast
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "scripts"), str(ROOT / "scripts/kat")]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for name in ("flow.tcl", "bd_axi.tcl", "README.md", "rtl/picorv32.v",
                 "firmware/common/startup.S", "firmware/suite/kat_suite.c",
                 "hls/src/mlkem1024_keccak_accel.cpp", "data/fixtures/cases.json",
                 "board/release/release_manifest.json", "skill/README.md"):
        assert (ROOT / name).is_file(), "Missing input: " + name
    checked = 0
    for folder in ("scripts", "hls/scripts", "pynq", "skill"):
        for path in (ROOT / folder).rglob("*.py"):
            ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
            checked += 1
    for folder in ("pynq", "board/release"):
        for path in (ROOT / folder).glob("*.ipynb"):
            notebook = json.loads(path.read_text(encoding="utf-8"))
            for cell in notebook["cells"]:
                if cell["cell_type"] == "code":
                    ast.parse("".join(cell["source"]), feature_version=(3, 6))
    print("PASS source paths, Python syntax (%d files) and notebooks" % checked)
    vendor = ROOT / "third_party/mlkem-native"
    manifest = json.loads((vendor / "SOURCE_MANIFEST.json").read_text())
    for item in manifest["files"]:
        assert sha(vendor / item["path"]) == item["sha256"], item["path"]
    bundle = ROOT / "board/release"
    release = json.loads((bundle / "release_manifest.json").read_text())
    for name, expected in release["files"].items():
        assert sha(bundle / name) == expected, "Release hash mismatch: " + name
    for name, expected in release.get("notebook_template_sha256", {}).items():
        assert sha(bundle / name) == expected, "Notebook template hash mismatch: " + name
    print("PASS pinned third-party source and paired board bundle hashes")
    from package_mlkem import load_cases, verify_roundtrip
    from collect_kat import expected_hardware, read_baseline
    cases, _ = load_cases(ROOT, 1024)
    fixture = json.loads((ROOT / "data/fixtures/cases.json").read_text())
    for expected, filename in ((False, "mlkem1024_input.mem"), (True, "mlkem1024_expected.mem")):
        verify_roundtrip(ROOT / "data/fixtures" / filename, fixture["cases"], 1024, expected)
    assert len(cases) == len(read_baseline(cases)) == len(expected_hardware()) == 145
    print("PASS official K4 vectors, fixtures, CPU reference and hardware call profile (145 cases)")
    print("PACKAGE_CHECK_PASS; no EDA process or board test was started")


if __name__ == "__main__":
    main()
