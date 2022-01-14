from _pytest.python_api import raises
from skeleton.commands import CreateDirectoryCommand, CreateFileCommand


import re


class MissingVersionError(Exception):
    pass


VERSION_MATCHER = re.compile(r"#\s*skel\d")


def create_parser(stream):
    first_line = stream.readline().strip()

    if not VERSION_MATCHER.match(first_line):
        raise MissingVersionError()

    # no parser choice logic needed right now
    return SkeletonParserV1(stream)


class SkeletonParserV1:
    def __init__(self, stream):
        self._stream = stream

    def parse(self):
        commands = []
        for line in self._stream:
            line = line.strip()
            if line.startswith("#"):
                continue
            if line.endswith("/"):
                commands.append(CreateDirectoryCommand(line))
            else:
                commands.append(CreateFileCommand(line))

        return commands
