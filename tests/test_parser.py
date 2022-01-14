from skeleton.parser import *
from io import StringIO
from skeleton.commands import *
import pytest


class TestParserCreation:
    def test_create_parser_throws_when_missing_version(self):
        file = StringIO("foo.txt\nbar")

        with pytest.raises(MissingVersionError):
            p = create_parser(file)

    def test_create_parser_consumes_version_and_returns_parser(self):
        # just testing for the only version, for now - expand if more versions are added
        file = StringIO("# skel1\nfoo.txt\nbar")

        p = create_parser(file)

        assert isinstance(p, SkeletonParserV1)
        assert file.readline() == "foo.txt\n"


class TestV1Parser:
    def test_parser_returns_commands_for_basic_file_creation(self):
        file = StringIO("foo.txt\nbar")
        p = SkeletonParserV1(file)

        commands = p.parse()

        assert len(commands) == 2
        assert isinstance(commands[0], CreateFileCommand)
        assert isinstance(commands[1], CreateFileCommand)
        assert commands[0].filepath == "foo.txt"
        assert commands[1].filepath == "bar"

    def test_parser_skips_comments(self):
        file = StringIO("foo.txt\n# a comment\nbar")
        p = SkeletonParserV1(file)

        commands = p.parse()

        assert len(commands) == 2

    def test_parser_preserves_full_path_for_file(self):
        file = StringIO("dir1/dir2/foo.txt")
        p = SkeletonParserV1(file)

        commands = p.parse()

        assert isinstance(commands[0], CreateFileCommand)
        assert commands[0].filepath == "dir1/dir2/foo.txt"

    def test_parser_returns_command_for_empty_directory(self):
        file = StringIO("dir1/\nparent/child/")
        p = SkeletonParserV1(file)

        commands = p.parse()

        assert len(commands) == 2
        assert isinstance(commands[0], CreateDirectoryCommand)
        assert isinstance(commands[1], CreateDirectoryCommand)
        assert commands[0].path == "dir1/"
        assert commands[1].path == "parent/child/"

    def test_parser_full_test(self):
        skel = """README.rst
LICENSE
setup.py
sample/__init__.py
sample/core.py
sample/helper/helper.py
empty/"""

        file = StringIO(skel)
        p = SkeletonParserV1(file)

        commands = p.parse()

        assert len(commands) == 7
        assert commands[1].filepath == "LICENSE"
        assert commands[3].filepath == "sample/__init__.py"
        assert commands[6].path == "empty/"
