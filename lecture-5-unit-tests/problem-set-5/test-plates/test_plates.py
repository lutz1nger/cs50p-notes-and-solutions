from plates import is_valid

def test_alphabetical_beginning():
    assert is_valid('CS50') == True
    assert is_valid('50') == False

def test_len():
    assert is_valid('AAAAA') == True
    assert is_valid('A') == False
    assert is_valid('AAAAAAAAA') == False

def test_numbers():
    assert is_valid('CS50') == True
    assert is_valid('CS50P') == False
    assert is_valid('CS05') == False

def test_alpanumerical():
    assert is_valid('CS50!') == False
