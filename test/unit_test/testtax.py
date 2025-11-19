import pytest
from src.pricing import add_tax

def test_add_tax_default_rate():
    assert add_tax(100.0) == pytest.approx(107.0)

def test_add_tax_custom_rate():
    assert add_tax(50.0, 0.1) == pytest.approx(55.0)

def test_add_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        add_tax(10.0, -0.01)
