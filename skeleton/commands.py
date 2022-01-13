class CommandContext:
    def __init__(self, current_dir) -> None:
        self._current_dir = current_dir

    @property
    def current_dir(self):
        return self._current_dir


class CreateFileCommand:
    def __init__(self, filename):
        self.filename = filename

    def run(self, context: CommandContext):
        path = context.current_dir / self.filename
        path.write_text("")
