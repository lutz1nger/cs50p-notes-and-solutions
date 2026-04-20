import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert('1/1') == 100
    with pytest.raises(ValueError):
        convert('10/1')
    with pytest.raises(ValueError):
        convert('-1/1')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'
