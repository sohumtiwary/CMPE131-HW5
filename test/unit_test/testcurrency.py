from src.pricing import format_currency

def test_format_currency_rounds_and_formats():
    assert format_currency(1) == "$1.00"
    assert format_currency(1.2) == "$1.20"
    assert format_currency(1.234) == "$1.23"   # rounds
    assert format_currency("2") == "$2.00"     # stringy numbers ok
