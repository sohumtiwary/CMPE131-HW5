import pytest
from src.pricing import apply_discount

def test_apply_discount_zero_percent():
    assert apply_discount(100.0, 0) == 100.0

def test_apply_discount_large_percent():
    assert apply_discount(200.0, 150) == -100.0

def test_apply_discount_negative_percent_raises():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5)
