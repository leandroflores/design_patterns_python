from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def name(self) -> str: ...


class Product1(Product):
    def name(self) -> str:
        return "Product 1"


class Product2(Product):
    def name(self) -> str:
        return "Product 2"


class Builder(ABC):
    @abstractmethod
    def reset(self) -> None: ...

    @abstractmethod
    def build_step_a(self) -> None: ...

    @abstractmethod
    def build_step_b(self) -> None: ...

    @abstractmethod
    def build_step_n(self) -> None: ...

    @abstractmethod
    def result(self) -> Product: ...


class Builder1(Builder):
    def __init__(self) -> None:
        super().__init__()
        self.product: Product = Product1()

    def reset(self) -> None:
        print("Reset Builder 1")

    def build_step_a(self) -> None:
        print("Build Step A of Builder 1")

    def build_step_b(self) -> None:
        print("Build Step B of Builder 1")

    def build_step_n(self) -> None:
        print("Build Step N of Builder 1")

    def result(self) -> Product:
        return self.product


class Builder2(Builder):
    def __init__(self) -> None:
        super().__init__()
        self.product: Product = Product2()

    def reset(self) -> None:
        print("Reset Builder 2")

    def build_step_a(self) -> None:
        print("Build Step A of Builder 2")

    def build_step_b(self) -> None:
        print("Build Step B of Builder 2")

    def build_step_n(self) -> None:
        print("Build Step N of Builder 2")

    def result(self) -> Product:
        return self.product


class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder: Builder = builder

    def change(self, builder: Builder) -> None:
        self.builder = builder

    def make(self, type: str) -> Product:
        self.builder.reset()
        if type == "sample":
            self.builder.build_step_a()
        else:
            self.builder.build_step_b()
            self.builder.build_step_n()
        return self.builder.result()


director = Director(Builder1())
print(director.make("sample"))
print(director.make("complete"))
print("")

director = Director(Builder2())
print(director.make("sample"))
print(director.make("complete"))
