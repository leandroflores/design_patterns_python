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


class PizzaBuilder:
    def __init__(self) -> None:
        self.size: PizzaSize = None
        self.crust: str = None
        self.toppings: list[str] = []
        self.sauce: str = None
        self.vegan: bool = False

    def build(self) -> Pizza:
        return Pizza(
            self.size,
            self.crust,
            self.toppings,
            self.sauce,
            self.vegan,
        )

    def set_size(self, size: PizzaSize) -> "PizzaBuilder":
        self.size = size
        return self

    def set_crust(self, crust: str) -> "PizzaBuilder":
        self.crust = crust
        return self

    def add_topping(self, topping: str) -> "PizzaBuilder":
        self.toppings.append(topping)
        return self

    def set_sauce(self, sauce: str) -> "PizzaBuilder":
        self.sauce = sauce
        return self

    def set_vegan(self, vegan: str) -> "PizzaBuilder":
        self.vegan = vegan
        return self


builder = PizzaBuilder()
pizza_1 = (
    builder.set_size(PizzaSize.BIG)
    .set_crust("Fina")
    .add_topping("Queijo")
    .add_topping("Bacon")
    .set_sauce("Molho Branco")
).build()
pizza_2 = (
    builder.set_size(PizzaSize.BIG)
    .set_crust("Fina")
    .add_topping("Queijo")
    .add_topping("Bacon")
    .set_sauce("Molho Branco")
).build()

print(pizza_1)
print(pizza_2)
