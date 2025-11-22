import os
import pathlib

from mktestdocs import check_md_file


def test_simple_fit():
    proj_dir = pathlib.Path(__file__).resolve().parent / ".."
    os.chdir(proj_dir / "examples" / "Basic Usage")
    fpath = proj_dir / "docs" / "tutorial" / "simple_fit.md"
    check_md_file(fpath=fpath, memory=True)
