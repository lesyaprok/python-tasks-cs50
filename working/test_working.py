from working import convert
import pytest

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:15 PM to 6:30 AM") == "22:15 to 06:30"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_convert_raises_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("8 AM - 15 PM")
    with pytest.raises(ValueError):
        convert("07:00 AM - 18:00 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_convert_other_cases():
     with pytest.raises(ValueError):
        convert("")
        convert("9 AM")
        convert("9:00AM to 10:00PM")
