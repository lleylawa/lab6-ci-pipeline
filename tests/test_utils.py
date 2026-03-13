from src.utils import is_even, is_positive


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False


def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-5) is False
