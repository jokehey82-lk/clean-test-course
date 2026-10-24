from types import SimpleNamespace

from api.controllers import Delivery


def make_order(*quantities):
    return [SimpleNamespace(quantity=quantity) for quantity in quantities]


def test_lots_of_items():
    order = make_order(5, 5, 5)

    assert Delivery.calculate(order, 6) == 7.50


def test_middle_of_the_road_items():
    order = make_order(2, 2, 2)

    assert Delivery.calculate(order, 4) == 5


def test_default_delivery_fee_is_3_50():
    order = make_order(2, 2)

    assert Delivery.calculate(order, 3) == 3.50


def test_default_delivery_fee_for_empty_order():
    assert Delivery.calculate([], 0) == 3.50