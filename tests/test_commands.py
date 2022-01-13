from skeleton.commands import *


class TestCreateFileCommand:
    def test_it_stores_filename(self):
        c = CreateFileCommand("foo.txt")

        assert c.filename == "foo.txt"

    def test_it_creates_empty_file_at_context_path(self, tmp_path):
        c = CreateFileCommand("foo.txt")

        c.run(CommandContext(tmp_path))

        expected = tmp_path / "foo.txt"
        assert len(list(tmp_path.iterdir())) == 1
        assert expected.exists()
        assert expected.read_text() == ""
