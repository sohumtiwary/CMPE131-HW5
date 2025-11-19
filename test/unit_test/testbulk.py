import pytest
from src.pricing import bulk_total

def test_bulk_total_simple_list():
    total = bulk_total([1, 2, 3], discount_percent=10, tax_rate=0.05)
    assert total == pytest.approx(5.67, rel=1e-9)
