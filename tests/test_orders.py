from orders import load_orders, get_next_order_id, save_order


def test_load_orders():
    orders = load_orders()
    assert isinstance(orders, list)


def test_get_next_order_id():
    orders = [
        {"order_id": "ORD1001"},
        {"order_id": "ORD1002"}
    ]

    assert get_next_order_id(orders) == "ORD1003"


def test_get_first_order_id():
    orders = []

    assert get_next_order_id(orders) == "ORD1001"


def test_save_order():
    orders = []

    order = {
        "name": "Aryan",
        "order_id": "ORD1001",
        "phone number": "9876543210",
        "address": "VIT Bhopal",
        "items": [{"id": 101, "quantity": 2}],
        "Total": 998
    }

    save_order(orders, order)

    assert len(orders) == 1
    assert orders[0]["order_id"] == "ORD1001"