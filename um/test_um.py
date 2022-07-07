from um import count

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um...") == 1

def test_count_case():
    assert count("Um, UM, um") == 3
    assert count("Umm, hello, UM... how are you?") == 1
    assert count("um! mU Um Mu") == 2

def test_count_case_no_matches():
    assert count("Yummi") == 0
    assert count("umumum") == 0
    assert count("sUMmer") == 0
