class CommandContext:
    def __init__(self, current_dir) -> None:
        self._current_dir = current_dir

    @property
    def current_dir(self):
        return self._current_dir


class CreateFileCommand:
    def __init__(self, filepath):
        self.filepath = filepath

    def run(self, context: CommandContext):
        path = context.current_dir / self.filepath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("")


class CreateDirectoryCommand:
    def __init__(self, path):
        self.path = path

    def run(self, context: CommandContext):
        path = context.current_dir / self.path
        path.mkdir(parents=True, exist_ok=True)
