# Builder

## Propósito

O ***Builder*** é um **padrão de projeto criacional** que permite a construção de objetos complexos passo a passo. O padrão permite que você produza diferentes tipos e representações de um objeto usando o mesmo código de construção.

## Problema

Considere um objeto complexo que necessite de uma inicialização passo a passo trabalhosa de muitos atributos e objetos agrupados. Normalmente, essa inicialização é feita por meio de parâmetros de um método construtor. Ou pior: espalhado pelo código cliente.

<html>
<img src="../../imagens/criacional/builder/builder_1.png" width="400" alt="Factory Method">
<p><b>Figura 1</b>: Representação de diferentes combinações possíveis para uma casa.</p>
</html>

Considere o cenário de um objeto `Casa`. Para construir uma `Casa` é preciso construir as paredes, piso, portas, janelas e o teto. No entanto, é possível um objeto `Casa` possuir jardim, piscina, garagem. A solução mais simples seria estender a classe base `Casa` e criar um subconjunto de casas com seu próprio construtor com seus parâmetros próprios. No entanto, isso pode resultar em um número extenso de subclasses e qualquer novo parâmetro exige uma alteração mais delicada na hierarquia.

Uma outra alternativa não fazendo uso de herança, seria criar um construtor gigante na classe base `Casa`, com todos os possíveis parâmetros para todos os tipos de casa. Porém, essa alternativa resulta em um novo problema: parte dos parâmetros não é usada e o construtor passa a ter muitos parâmetros desnecessários.

## Solução

O padrão ***Builder*** apresenta a extração do código de construção de objetos para fora da própria classe para uma classe separada chamada ***builer***. O termo ***builder*** refere-se exatamente à ***construtor***, mas é completamente diferente do método construtor.

O padrão ***Builder*** organiza a construção de objetos em uma série de etapas. No exemplo da `Casa`, podemos organizar em métodos: `construirParedes`, `assentarPiso`, etc. Portanto, para criar um objeto, é necessário executar uma série de etapas do objeto ***builder***. A parte importante é a possibilidade de executar somente as etapas pertinentes ao objeto.

Algumas partes da construção podem possuir implementações diferentes na criação de objetos. Tal contexto permite a criação de diferentes ***builders*** com os mesmos métodos, mas implementados de forma diferente. Assim, esse ***builder*** pode ser usado em conjunto no processo de construção de uma casa. No exemplo da `Casa`, imagine um ***builder*** que construa de madeira e vidro, um outro ***builder*** que constrói com pedra e ferro e um terceiro ***builder*** que constrói com ouro e prata. Ao chamar o mesmo conjunto de etapas que resulta em três casas distintas.

Uma variação do padrão ***Builder*** é o uso de uma classe **Diretor**. É possível extrair uma série de chamadas para a classe **diretor**. A **Classe Diretor** define a ordem de execução das etapas, enquanto as **classes *builder*** implementa as etapas.

O uso da **Classe Diretor** é optativo, porém é interessante por centralizar o processamento (reutilização) e por esconder os detalhes da construção do produto do código cliente (encapsulamento). O cliente precisa apenas passar o ***builder*** para o **diretor**, inicializar a construção com o **diretor** e esperar o resultado.

## Implementação

A implementação do ***Builder*** não é definida por um algoritmo, mas pode ser descrita por alguns passos:
- Abstraia as etapas claras para a construção de diferentes classes de produto.
- Declare essas etapas na **interface *Builder***.
- Crie uma classe ***Builder* Concreta** para cada representação do produto e implemente suas etapas de construção e o resultado. O resultado da construção pode ser definido no ***Builder* Base** quando os produtos são da mesma hierarquia. Caso contrário, é necessário declarar o método do resultado nos diferentes ***Builders** Concretos*.
- Considere a possibilidade de agrupar os passos de construção para a **Classe Diretor**.

A Figura 2 apresenta o diagrama com a solução do padrão ***Builder***.

<html>
<img src="../../imagens/criacional/builder/builder_2.png" width="400" alt="Builder">
<p><b>Figura 2</b>: Diagrama com a definição do <i>Builder</i>.</p>
</html>

A interface ***Builder*** deve declarar as etapas de construção do produto, que são comuns a todos os tipos de ***buiders***. ***Builders* Concretos** fornecem diferentes implementações para as etapas de construção. ***Builders* Concretos** podem produzir produtos que não seguem a interface em comum.

**Produtos** são os objetos resultantes dos ***builders* concretos**. Os **Produtos** construídos por diferentes ***builders*** não precisam pertencer à mesma interface ou hierarquia de classe.

A **Classe Diretor** define a ordem na qual as etapas da construção são chamadas. É possível criar e reutilizar configurações específicas de produtos. O **Cliente** deve associar um dos ***builders*** com a **Classe Diretor**. Normalmente, é feito por meio dos parâmetros do construtor do diretor, existindo um único ***builder*** para todas as construções. 

A implementação em Python segue abaixo:

```python

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
```

## Exemplo Prático

Considere o cenário de um software para pizzaria. A pizza pode ter variações: tamanho, massa, sabor, molho e se é vegana ou não. Uma solução simplificada é apresentada a seguir:

```python

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


pizza_1 = Pizza(PizzaSize.BIG, "Fina", ["Queijo", "Bacon"], "Molho Branco", False)
pizza_2 = Pizza(PizzaSize.SMALL, "Grossa", ["Rucula"], "Molho Vermelho", True)

print(pizza_1)
print(pizza_2)

```
No exemplo apresentado, a criação de uma pizza requer todos os parâmetros passados para o construtor. A confusão é causada pelos pedidos maiores e mais complexos, além da falta de flexibilidade por exigir a passagem de parâmetros estritamente definida. 

O exemplo a seguir apresenta a refatoração com o padrão ***Builder***:

```python
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

```

No exemplo apresentado, o ***Builder*** atua como o construtor do objeto, reduzindo a complexidade na chamada para o construtor diretamente pelo cliente.

## Discussão

O padrão ***Builder*** é muito aplicado em situações com um número extenso de parâmetros para o construtor. A chamada de construtores com muitos parâmetros. Este cenário passa a ser incoveniente pelo fato de exigir sobrecarga de construtores ou uso de parâmetros desnecessários, com versões alternativas de parâmetros de acordo com o produto final. O fato do padrão ***Builder*** construir objetos em etapas, não é necessário fazer uso de construtores com múltiplos parâmetros.

O padrão ***Builder*** permite a criação de diferentes representações do mesmo produto, em especial, quando existe uma série de etapas semelhantes para a criação. Isso é possível pela interface base do ***Builder*** definir todas as etapas possíveis, e os ***builders* concretos** são responsáveis por definir os detalhes da etapa.

O padrão ***Builder*** por permitir a criação por etapas é muito indicado na construção de objetos complexos. É possível adiar a execução de etapas da interface base sem quebrar o produto final. Por meio da recursão, é possível construir árvores de objetos. O ***Builder*** não retorna o produto final até o processo ser concluído, previnindo o retorno de um produto final incompleto.


## Conclusão

O ***Builder*** é um padrão de projeto criacional, que permite a construção de objetos complexos passo a passo. O ***Builder*** não exige que os produtos tenham uma interface comum. Isso torna possível produzir produtos diferentes usando o mesmo processo de construção.

As principais vantagens do padrão de projeto ***Builder*** são:
- Construir objetos por etapas, adiando etapas de construção e possibilidade de chamadas recursivas.
- Reutilizar o mesmo código de construção para várias representações de produtos.
- **Princípio de Responsabilidade Única**: o código de construção do objeto é isolado da lógica de negócio.

No entanto, o maior desafio é a complexidade do código conforme existam múltiplas classes novas.

