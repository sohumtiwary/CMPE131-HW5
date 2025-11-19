from src.order_io import load_order, write_receipt

def test_order_integration(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    items = load_order(input_file)
    # also checks parse_price interaction
    assert items == [("widget", 10.0), ("gizmo", 5.50)]

    receipt_path = tmp_path / "receipt.txt"
    write_receipt(receipt_path, items, discount_percent=10, tax_rate=0.1)

    output_text = receipt_path.read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert "TOTAL: $" in output_text  # format check
