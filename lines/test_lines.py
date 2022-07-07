import pytest
from lines import count_file_lines

def test_count_file_lines():
    with pytest.raises(SystemExit):
        count_file_lines("non_existent_file.py")
    assert count_file_lines("hello.py") == 1