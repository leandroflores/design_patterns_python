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


class DeliveryFactory:
    @staticmethod
    def create_delivery(delivery_type: str) -> Delivery:
        if delivery_type == "fast":
            return FastDelivery()
        if delivery_type == "default":
            return DefaultDelivery()
        if delivery_type == "economic":
            return EconomicDelivery()
        raise ValueError("Delivery Type not found")


def create_order(delivery_type: str, distance: float) -> float:
    delivery = DeliveryFactory(delivery_type)
    return delivery.get_price(distance)
