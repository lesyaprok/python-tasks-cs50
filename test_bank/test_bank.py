from bank import value

def test_hello():
    assert value("Hello!") == 0
    assert value("heLLo!") == 0
    assert value("hello") == 0

def test_starts_with_h():
    assert value("Hola") == 20
    assert value("hi!!!") == 20
    assert value("Lalala") != 20

def test_other_greetings():
    assert value("Good evening") == 100
    assert value("Hello there") != 100
    assert value("Morning") == 100

def test_other_languages():
    assert value("Здравствуйте") == 100
    assert value("嘿") == 100
    assert value("Buenos días") == 100