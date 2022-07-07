from numb3rs import validate

def test_validate():
    assert validate("255.255.255.0")
    assert validate("127.0.0.1")
    assert not validate("275.3.6.28")
    assert validate("0.0.0.0")
    assert not validate("512.512.512.512")
    assert not validate("1.2.3.1000")
    assert not validate("256.0.0.0")
    assert not validate("0.256.0.0")

def test_validate_invalid_input():
    assert not validate("2.2.2.")
    assert not validate("....")
    assert not validate("128..5.0")

def test_validate_non_numeric():
    assert not validate("cat")
    assert not validate("O.O.O.O")
