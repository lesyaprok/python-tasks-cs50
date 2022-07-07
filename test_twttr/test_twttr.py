from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("twttr") == "twttr"
    assert shorten("") == ""
    assert shorten("AeiOuI") == ""
    assert shorten("Check how this function works") == "Chck hw ths fnctn wrks"

def test_upper():
    assert shorten("twIttEr") == "twttr"
    assert shorten("IAEOU") == ""

def test_lower():
    assert shorten("banana") == "bnn"
    assert shorten("iaeou") == ""

def test_numbers():
    assert shorten("1234aei") == "1234"

def test_punctuation():
    assert shorten("aa,ee,ou!") == ",,!"
