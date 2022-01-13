from skeleton.parser import SkeletonParserV1
from io import StringIO
from skeleton.commands import *


def test_parser_returns_commands_for_basic_file_creation():
    file = StringIO("foo.txt\nbar")
    p = SkeletonParserV1(file)

    commands = p.parse()

    assert len(commands) == 2
    assert isinstance(commands[0], CreateFileCommand)
    assert isinstance(commands[1], CreateFileCommand)
    assert commands[0].filename == "foo.txt"
    assert commands[1].filename == "bar"
