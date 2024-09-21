from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def doStuff(self) -> str: ...


class ConcreteProductA(Product):
    def doStuff(self) -> str:
        return "Do stuff Product A"


class ConcreteProductB(Product):
    def doStuff(self) -> str:
        return "Do stuff Product B"


class Creator(ABC):
    @abstractmethod
    def create_product(self) -> Product: ...

    def some_operation(self) -> str:
        return "Creator"


class ConcreteCreatorA(Creator):
    def create_product(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def create_product(self) -> Product:
        return ConcreteProductB()
