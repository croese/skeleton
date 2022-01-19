from skeleton.skeleton import extract_args
from pathlib import Path
import pytest


def test_accepts_optional_root_path():
    actual = extract_args(["myskel"])
    expected = Path(".")
    assert expected == actual.root

    actual = extract_args(["--root", "dir1/dir2", "myskel"])
    expected = Path("dir1/dir2")
    assert expected == actual.root

    actual = extract_args(["-r", "dir1/dir2", "myskel"])
    expected = Path("dir1/dir2")
    assert expected == actual.root


def test_accepts_file_argument():
    actual = extract_args(["--file", "dir1/foo.skel"])
    expected = Path("dir1/foo.skel")
    assert expected == actual.file

    actual = extract_args(["-f", "dir1/foo.skel"])
    expected = Path("dir1/foo.skel")
    assert expected == actual.file


def test_accepts_name_positional_argument():
    actual = extract_args(["myskel"])
    assert actual.name == "myskel"


def test_either_file_or_name_are_required():
    with pytest.raises(SystemExit):
        extract_args([])
