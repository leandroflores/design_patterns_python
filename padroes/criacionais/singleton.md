# Singleton

## Propósito

O ***Singleton*** é um **padrão de projeto criacional** que permite que uma classe possua uma instância única, fornecendo acesso global à essa instância para os clientes.

A Figura 1 apresenta uma metáfora com o cenário da aplicação do padrão ***Singleton***.

![Exemplo do padrão ***Singleton***](../../imagens/criacionais/singleton/singleton_1.png)
**Figura 1:** Representação visual do padrão ***Singleton***.

## Problema

O padrão ***Singleton*** garante que uma classe possua apenas uma única instância. Esse cenário é aplicado especialmente em casos que se faz necessário o acesso à determinado recurso compartilhado. Como exemplo de aplicação, é possível citar arquivos extensos de texto e sessões de banco de dados.

O padrão ***Singleton*** também fornece um ponto de acesso global para a única instância. Uma forma de proteção é a classe ***Singleton*** acoplar o valor da instância para evitar sobrescrita e exposição dos valores, além de impedir que o código fique espalhado pelo código.

A Figura 2 apresenta um exemplo de cliente consultando a instância única do padrão ***Singleton***.

![Clientes no padrão ***Singleton***](../../imagens/criacionais/singleton/singleton_2.png)
**Figura 2:** Clientes consultando instância única do padrão ***Singleton***.

No entanto, o padrão ***Singleton*** resolve dois problemas de uma vez, violando o **Princípio de Responsabilidade Única**.

## Solução

A solução proposta pelo padrão ***Singleton*** apresenta a definição de um construtor padrão privado, evitando a instanciação de objetos diretamente pelo construtor a partir do código cliente.

Além disso, é definido um método estático que atua como construtor. Este método chama o construtor privado, instancia o objeto e salva em um atributo estático, armazenando esse objeto em *cache* e retornando esse objeto para futuras chamadas.

## Implementação

Para aplicar o padrão ***Singleton*** é necessário seguir as seguintes etapas:

- Adicione um atributo privado estático na classe ***Singleton***.
- Declare um método de criação público estático para obter a instância ***Singleton***.
- Implemente a instanciação do objeto em sua primeira chamada e armazene o objeto em um atributo estático, que será retornado em futuras chamadas.
- Deixe o construtor privado, impedindo chamadas de fora da classe ***Singleton***.
- Em todas as chamadas pelo **Cliente**, substitua a chamada do construtor pela chamada do método estático da classe ***Singleton***.

A Figura 3 apresenta o diagrama com a solução do padrão ***Singleton***.

![Arquitetura ***Singleton***](../../imagens/criacionais/singleton/singleton_3.png)
**Figura 3:** Arquitetura do padrão ***Singleton***.

A classe ***Singleton*** declara o método estático que retorna a instância única da classe. O construtor deve ser privado para não ser chamado fora da classe ***Singleton***. O acesso ao objeto só é possível pelo método estático.

A implementação em Python segue abaixo:

```python
class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args: object, **kwds: object) -> object:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Running logic...")


if __name__ == "__main__":
    s1: Singleton = Singleton()
    s2: Singleton = Singleton()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
```

## Exemplo Prático

Considere um exemplo para criação de uma conexão com Banco de Dados. Uma solução sem uso de ***Singleton*** é apresentado a seguir:

```python

class Session:

    def __init__(self) -> None:
        self.host: str = "localhost"
        self.user: str = "root"
        self.port: str = "5403"

session_1 = Session()
session_2 = Session()

print(id(session_1))
print(id(session_2))
print(id(session_1) == id(session_2))

```

Os identificadores são diferentes, ou seja, as instâncias são diferentes. Portanto, toda vez é criado um objeto novo, não fazendo uso de uma única instância.

O exemplo a seguir apresenta a refatoração com o padrão ***Singleton***:

```python
class SessionSingleton:
    _instance: "SessionSingleton" = None

    def __init__(self) -> None:
        self.host: str = "localhost"
        self.user: str = "root"
        self.port: str = "5403"

    @classmethod
    def instance(cls) -> "SessionSingleton":
        if not cls._instance:
            cls._instance = cls()
        return cls._instance


session_1: SessionSingleton = SessionSingleton.instance()
session_2: SessionSingleton = SessionSingleton.instance()

print(id(session_1))
print(id(session_2))
print(id(session_1) == id(session_2))

```

Nesse caso, a instância é inicializada uma única vez, e essa instância única é retornada toda vez pelo método estático.

## Discussão

O padrão ***Singleton*** é voltados para contextos em que seu programa precisa de uma única instância disponível para todos os clientes. Outra razão é a necessidade de existir um controle mais restrito sobre o acesso à variáveis globais.

Dentre os pontos positivos da aplicação do ***Singleton*** temos:

- Certeza que uma classe terá somente uma única instância.
- Ponto de acesso global para a instância.
- Objeto inicializado somente na primeira chamada do método.

E entre os pontos negativos temos:

- Não segue o princípio de responsabilidade única, resolvendo dois problemas de uma vez.
- Pode mascarar um *design* ineficiente, quando os componentes do programa sabem muito sobre cada um.
- Requer tratamento especial em um ambiente *multithreaded*, para que múltiplas *threads* não possam criar vários objetos.
- Dificuldade em fazer testes unitários.

## Conclusão

O ***Singleton*** é um padrão de projeto criacional que garante uma instância única para a classe, fornecendo um ponto de acesso único à instância no sistema.

O padrão ***Singleton*** é muito similar ao conceito de variável global.

O padrão ***Singleton*** é útil para proteger o acesso e a implementação lógica da instanciação do objeto única de uma classe.
