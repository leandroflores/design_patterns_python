from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype": ...


class ConcretePrototype(Prototype):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name

    def clone(self) -> "ConcretePrototype":
        copy_name: str = deepcopy(self.name)
        prototype: ConcretePrototype = ConcretePrototype(copy_name)
        return prototype


prototype = ConcretePrototype("Peter")
copy = prototype.clone()

print(id(prototype))
print(id(copy))
