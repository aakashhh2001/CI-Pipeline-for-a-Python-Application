import pytest
from utils import add_numbers, reverse_string

def test_add_positive():
    assert add_numbers(5, 7) == 12

def test_add_negative():
    assert add_numbers(-5, -5) == -10

def test_reverse_text():
    assert reverse_string("abc") == "cba"
