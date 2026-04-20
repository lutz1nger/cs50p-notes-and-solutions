from twttr import shorten

def test_lowercase():
    assert shorten('xaeoiuy') == 'xy'

def test_uppercase():
    assert shorten('XAEOIUY') == 'XY'

def test_numbers():
    assert shorten('123') == '123'

def test_punctuation():
    assert shorten('.') == '.'
