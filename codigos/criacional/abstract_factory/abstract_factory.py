from abc import ABC, abstractmethod


class ProductA(ABC):
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def operation_a(self) -> None: ...


class ProductB(ABC):
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def operation_b(self) -> None: ...


class ConcreteProductA1(ProductA):
    def name(self) -> str:
        return "Product A1"

    def operation_a(self) -> None:
        print("Operation A1")


class ConcreteProductA2(ProductA):
    def name(self) -> str:
        return "Product A2"

    def operation_a(self) -> None:
        print("Operation A2")


class ConcreteProductB1(ProductB):
    def name(self) -> str:
        return "Product B1"

    def operation_b(self) -> None:
        print("Operation B1")


class ConcreteProductB2(ProductB):
    def name(self) -> str:
        return "Product B2"

    def operation_b(self) -> None:
        print("Operation B2")


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> ProductA: ...

    @abstractmethod
    def create_product_b(self) -> ProductB: ...


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB2()


class Client:
    def __init__(self, factory: AbstractFactory) -> None:
        self._factory: AbstractFactory = factory

    def operation(self) -> None:
        print(self._factory.create_product_a().name())
        print(self._factory.create_product_b().name())


# Tests:

client = Client(ConcreteFactory1())
client.operation()

print("-" * 50)

client = Client(ConcreteFactory2())
client.operation()
