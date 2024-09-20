# Prototype

## Propósito

O ***Prototype*** é um **padrão de projeto criacional** que permite copiar objetos existentes sem fazer seu código ficar dependente de suas classes.

## Problema

Considere a necessidade de criar a cópia exata de um objeto. O primeiro passo é criar um novo objeto da mesma classe. Posteriormente, passar por todos os atributos do objeto original e copiar seus valores para o novo objeto.

Porém, considere o cenário de atributos privados, em que não é possível acessá-los fora do escopo do próprio objeto.

A Figura 1 apresenta uma metáfora sobre as dificuldades de fazer uma cópia de um objeto.

![Metáfora de cópia de objetos](../../imagens/prototype/prototype_1.png)
**Figura 1:** Exemplo de problema na cópia de objetos.

Outro problema é que a necessidade de saber exatamente a classe do objeto original para criar uma cópia, configura uma dependência. Em casos que a dependência segue o tipo de uma interface, é impossível saber a classe exata.

## Solução

O padrão ***Prototype*** transmite o processo de cópia para o próprio objeto a ser clonado. O padrão declara uma interface comum para todas as classes que podem ter objetos a ser clonados. Essa interface permite a chamada do método que faz a cópia, sem acoplar seu código à classe do objeto. Normalmente, a interface possui um único método: `clonar`.

A implementação do método `clonar` é muito parecida em todas as classes. O método cria um objeto da classe atual e copia todos os valores dos atributos para o novo objeto, incluindo os atributos privados da classe. Um objeto que suporta clonagem é chamado de **protótipo**. Para objetos extensos, com muitos atributos, torná-lo um **protótipo** é uma alternativa viável.

## Implementação

A aplicação do ***Prototype*** é descrito pelas seguintes etapas:

- Crie uma interface protótipo e declare o método `clonar`.
- A classe protótipo deve definir um construtor alternativo que aceita um objeto daquela classe como argumento. O construtor deve copiar os valores de todos os atributos definidos na classe do objeto passado para a nova instância.
- O método de clonagem executa a instanciação com a versão do protótipo do construtor. Toda clase deve sobrescrever o método `clonar` e usar sua proṕria classe, para não resultar em uma clonagem da classe superior.
- Caso necessário, crie um registro protótipo centralizado para armazenar um conjunto de protótipos que são usados com frequência. O registro pode ser usado com uma classe *factory* ou método estático. É possível associar um valor (*String*) para retornar uma cópia do protótipo para o cliente.

A Figura 2 apresenta a arquitetura do padrão ***Prototype***.

![Solução com ***Prototype***](../../imagens/criacional/prototype/prototype_2.png)
**Figura 2:** Arquitetura do padrão ***Prototype***.

A interface ***Prototype*** declara os métodos de clonagem. A classe **Protótipo Concreta** implementa o método de clonagem. Além da cópia dos atributos do objeto original, pode incluir a cópia específica de outros objetos relacionados. O **Cliente** pode produzir uma cópia de qualquer objeto que implementa a interface do **Protótipo**.

A implementação em Python segue abaixo:

```python

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

```

## Exemplo Prático

Considere o cenário de um software para concessária de veículos. Considerando os atributos marca, modelo, cor e ano, temos o seguinte código:

```python

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

```

Em um contexto com necessário de várias instanciações, com carros parecidos, passa-se a ter uma repetição de código frequente.

O exemplo a seguir apresenta a refatoração com o padrão ***Prototype***:

```python
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

```

No exemplo apresentado, a instanciação é mais simplicada pelo fato de partir de uma base pré-definida por meio do ***Prototype***.

## Discussão

O padrão ***Prototype*** permite o processo de cópia de objetos sem acoplar codigo às classes concretas. A principal vantagem é se livrar de códigos de inicialização repetidos por protótipos pré-definidos.

Em caso de objetos mais complexos, é possível fazer o processo de forma mais específica, sendo possível especializar implementações por meio de herança.

## Conclusão

O ***Prototype*** é um padrão de projeto criacional que permite a clonagem de objetos, mesmo complexos, sem acoplamento à suas classes específicas.

Todas as **Classes de Protótipo** (***Prototypes***) devem ter uma interface comum que declare o método de clonagem do objeto, mesmo que as classes concretas sejam desconhecidas. Objetos protótipos podem produzir cópias completas, pois objetos da mesma classe podem acessar atributos privados.
