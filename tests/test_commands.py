from skeleton.commands import *


class TestCreateFileCommand:
    def test_it_stores_filename(self):
        c = CreateFileCommand("foo.txt")

        assert c.filepath == "foo.txt"

    def test_it_creates_empty_file_at_context_path(self, tmp_path):
        c = CreateFileCommand("foo.txt")

        c.run(CommandContext(tmp_path))

        expected = tmp_path / "foo.txt"
        assert len(list(tmp_path.iterdir())) == 1
        assert expected.exists()
        assert expected.read_text() == ""

    def test_it_creates_empty_file_at_nested_path(self, tmp_path):
        c = CreateFileCommand("dir1/dir2/foo.txt")

        c.run(CommandContext(tmp_path))

        expected = tmp_path / "dir1" / "dir2" / "foo.txt"
        assert expected.exists()
        assert expected.read_text() == ""


class TestCreateDirectoryCommand:
    def test_it_creates_empty_directory(self, tmp_path):
        c = CreateDirectoryCommand("dir1")

        c.run(CommandContext(tmp_path))

        expected = tmp_path / "dir1"
        assert expected.exists()
        assert expected.is_dir()
