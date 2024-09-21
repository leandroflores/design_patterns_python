from copy import deepcopy


class PrototypeCar:
    def __init__(
        self,
        brand: str,
        model: str,
        color: str,
        year: int,
    ) -> None:
        self.brand: str = brand
        self.model: str = model
        self.color: str = color
        self.year: int = year

    def clone(self) -> "PrototypeCar":
        return deepcopy(self)

    def __str__(self) -> str:
        return f"{self.brand} - {self.model} {self.year} ({self.color})"


prototype: PrototypeCar = PrototypeCar(
    "Toyota",
    "Corolla",
    "Black",
    2014,
)
car_1: PrototypeCar = prototype.clone()
car_2: PrototypeCar = prototype.clone()
car_2.color = "White"

print(car_1)
print(car_2)
