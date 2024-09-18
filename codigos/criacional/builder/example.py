from enum import Enum


class PizzaSize(Enum):
    BIG = "Grande"
    SMALL = "Pequena"


class Pizza:
    def __init__(
        self,
        size: PizzaSize,
        crust: str,
        toppings: list[str],
        sauce: str,
        vegan: bool,
    ) -> None:
        self.size: PizzaSize = size
        self.crust: str = crust
        self.toppings: list[str] = toppings
        self.sauce: str = sauce
        self.vegan: bool = bool

    def __str__(self):
        return f"Pizza {self.size}, {self.crust} crust, toppings: {self.toppings}, sauce: {self.sauce}, vegan: {self.vegan}"


pizza1 = Pizza(PizzaSize.BIG, "Fina", ["Queijo", "Bacon"], "Molho Branco", False)
pizza2 = Pizza(PizzaSize.SMALL, "Grossa", ["Rucula"], "Molho Vermelho", True)
