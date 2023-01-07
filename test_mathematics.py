import pytest

from mathematics import add_numbers, square_number, subtract_numbers

def test_add_positive():
    assert add_numbers(1, 2) == 3

def test_add_zero():
    assert add_numbers(1, 0) == 1

def test_add_negative():
    assert add_numbers(4, -100) == -96

def test_add_string__expect_exception():
    with pytest.raises(TypeError):
        add_numbers(4, 'I DO NOT BELONG HERE')

def test_square():
    assert square_number(3) == 9

def test_subtract():
    assert subtract_numbers(3,2) == 1

def test_subtract2():
    assert subtract_numbers(1, 5) == -4