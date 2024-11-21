from abc import ABC, abstractmethod

class ProductA(ABC):
    
    @abstractmethod
    def to_str(self) -> str:
        ...

    def __repr__(self) -> str:
        return self.to_str()

class ProductA1(ProductA):
    
    def to_str(self) -> str:
        return "Product A1"
    

class ProductA2(ProductA):
    
    def to_str(self) -> str:
        return "Product A2"

class ProductB(ABC):

    @abstractmethod
    def to_str(self) -> str:
        ...

    def __repr__(self) -> str:
        return self.to_str()

class ProductB1(ProductB):
    
    def to_str(self) -> str:
        return "Product B1"

class ProductB2(ProductB):
    
    def to_str(self) -> str:
        return "Product B2"

class AbstractFactory(ABC):

    @abstractmethod
    def create_product_A(self) -> ProductA:
        ...

    @abstractmethod
    def create_product_B(self) -> ProductB:
        ...

class ConcreteFactory1(AbstractFactory):

    def create_product_A(self) -> ProductA:
        return ProductA1()
    
    def create_product_B(self) -> ProductB:
        return ProductB1()
    
class ConcreteFactory2(AbstractFactory):

    def create_product_A(self) -> ProductA:
        return ProductA2()
    
    def create_product_B(self) -> ProductB:
        return ProductB2()
    
class Client:

    def __init__(self, factory: AbstractFactory) -> None:
        self.factory: AbstractFactory = factory

    def some_operation(self) -> None:
        ...

client_1 = Client(factory=ConcreteFactory1())

print(client_1.factory.create_product_A())
print(client_1.factory.create_product_B())

client_2 = Client(factory=ConcreteFactory2())
print(client_2.factory.create_product_A())
print(client_2.factory.create_product_B())