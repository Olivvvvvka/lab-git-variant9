import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from copy_file import safe_copy

def test_safe_copy_success():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, "src.txt")
        with open(src, "w", encoding="utf-8") as f:
            f.write("test")
        result = safe_copy(src)
        assert result is True
        dst = "src.txt"
        assert os.path.exists(dst)
        os.remove(dst)

def test_safe_copy_file_not_found():
    result = safe_copy("nonexistent_file_12345.txt")
    assert result is False