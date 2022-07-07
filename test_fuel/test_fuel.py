from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("0/3") == 0
    assert convert("4/4") == 100

def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("4/3")
        convert("one/four")
        convert("2.5/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
        convert("0/0")

def test_rauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
