class Car:
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

    def __str__(self) -> str:
        return f"{self.brand} - {self.model} {self.year} ({self.color})"


car_1: Car = Car("Toyota", "Corolla", "Black", 2014)
car_2: Car = Car("Toyota", "Hilux", "White", 2020)

print(car_1)
print(car_2)
