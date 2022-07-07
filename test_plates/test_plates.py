from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("CS50")
    assert not is_valid("n345")
    assert is_valid("NM33")

def test_length():
    assert not is_valid("m")
    assert is_valid("NN")
    assert not is_valid("FF2389008")

def test_numbers_in_the_middle():
    assert is_valid("AAA222")
    assert not is_valid("AAA22A")

def test_numbers_from_zero():
    assert not is_valid("CS05")

def test_punctuation():
    assert not is_valid("PI3.14")
    assert not is_valid("CS 50")
    assert not is_valid("A AA20")
    assert not is_valid("AAA222!")
    assert is_valid("RT34")
