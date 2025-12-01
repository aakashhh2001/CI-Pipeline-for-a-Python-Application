import pytest
from utils import add_numbers, reverse_string

def test_add_invalid_input():
    with pytest.raises(ValueError):
        add_numbers("x", 5)

def test_reverse_invalid_input():
    with pytest.raises(ValueError):
        reverse_string(12345)
