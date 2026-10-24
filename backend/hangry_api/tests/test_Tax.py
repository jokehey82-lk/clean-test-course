from api.controllers import Tax


def test_simple_tax_with_default_delivery_fee():
    subtotal = 15
    delivery_fee = 3.50

    tax = Tax.calculate(subtotal, delivery_fee)

    assert tax == 1.53