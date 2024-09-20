from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def get_price(self, distance: float) -> float: ...


class FastDelivery(Delivery):
    def get_price(self, distance: float) -> float:
        start_price: float = 10.00
        km_price: float = 5.00
        return start_price + km_price * distance


class DefaultDelivery(Delivery):
    def get_price(self, distance: float) -> float:
        start_price: float = 5.00
        km_price: float = 2.00
        return start_price + km_price * distance


class EconomicDelivery(Delivery):
    def get_price(self, distance: float) -> float:
        start_price: float = 2.00
        km_price: float = 1.00
        return start_price + km_price * distance


def create_order(delivery_type: str, distance: float) -> float:
    if delivery_type == "fast":
        delivery = FastDelivery()
    elif delivery_type == "default":
        delivery = DefaultDelivery()
    elif delivery_type == "economic":
        delivery = EconomicDelivery()
    else:
        raise ValueError("Delivery Type not found")
    return delivery.get_price(distance)
