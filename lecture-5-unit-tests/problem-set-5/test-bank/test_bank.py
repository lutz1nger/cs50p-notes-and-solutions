from bank import value

def test_uppercase():
    assert value('HELLO') == 0
    assert value('H') == 20
    assert value('CAT') == 100

def test_lowercase():
    assert value('hello') == 0
    assert value('h') == 20
    assert value('cat') == 100

def test_phrase():
    assert value('hello hello') == 0
    assert value('h h') == 20
    assert value('cat cat') == 100
