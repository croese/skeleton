from skeleton.commands import CreateFileCommand


class SkeletonParserV1:
    def __init__(self, stream):
        self._stream = stream

    def parse(self):
        commands = []
        for line in self._stream:
            commands.append(CreateFileCommand(line.strip()))

        return commands
