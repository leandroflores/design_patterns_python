# Adapter

## Propósito

O ***Adapter*** é um **padrão de projeto estrutural** que permite objetos com interfaces incompatíveis colaborarem entre si.

## Problema

Considere o seguinte cenário: uma aplicação de monitoramento do mercado de ações da bolsa. A aplicação busca os dados de fornecedores em formato XML e apresenta os gráficos e diagramas. Em certo momento, a aplicação passa a integrar uma biblioteca que trabalha apenas com dados JSON. Então, chega um ponto em que existe incompatibilidade entre os dados, e simultaneamente busca não alterar o código que trabalha com XML, mas precisa integrar para o trabalho de dados em JSON.

A Figura 1 apresenta o contexto do problema.

![Incompatibilidade de Tipos](../../imagens/estruturais/adapter/adapter_1.png)
**Figura 1:** Problema com arquivos em formatos distintos.

## Solução

O padrão ***Adapter*** propõe a definição de um **adaptador**. O **adaptador** é um objeto especial que converte a interface de um objeto para que outro possa estendê-lo.

Um **Adaptador** encobre um dos objetos para esconder a complexidade da conversão que acontece nos bastidores. O objeto encobrido nem fica sabendo do **adaptador**. Um exemplo seria encobrir um objeto que mede em m/s e km/h para um adaptador que trabalha unicamente com milhas/s.

Adaptadores podem não só converter dados em vários formatos, mas também pode ajudar objetos com diferentes interfaces a colaborar. Pode ser resumido em três passos:

* O adaptador obtém uma **interface**, compatível com um dos objetos existentes.
* Usando essa interface, o objeto existente pode chamar os métodos do **adaptador** com segurança.
* Ao receber a chamada, o **adaptador** passa o pedido para o segundo objeto, mas em um formato e ordem que o segundo objeto espera.

A Figura 2 apresenta uma solução para o problema do mercado de ações, sendo que as classes centrais são manipuladas em XML e uma interface adapter faz a comunicação com a fonte em JSON.


![Fábricas Concretas](../../imagens/estruturais/adapter/adapter_2.png)
**Figura 2:** Software para mercado de ações com o ***Adapter***.

Um exemplo real são os diferentes padrões de tomada em diversos lugares do mundo.

## Implementação

A implementação do ***Adapter*** pode ser organizada pelos seguintes passos:

- Certifique que existem ao menos duas classes com interfaces incompatíveis:
  - Uma classe **serviço** útil, sem a opção de alteração.
  - Uma ou mais classes **cliente** que seriam beneficiadas com o uso da classe **serviço**.
- Declare a **interface cliente** e descreva como o **cliente** se comunica com o **serviço**.
- Crie a **classe adaptadora** e **implemente** a **interface cliente**, com os métodos vazios inicialmente.
- Adicione um campo para a classe do **adaptador** para armazenar uma referência ao objeto do serviço. A prática comum é inicializar esse campo com o construtor, porém, é mais conveniente passá-lo para o **adaptador** ao chamar seus métodos.
- Individualmente implemente todos os **métodos abstratos** da **interface cliente** na **classe adaptadora**. O **adaptador** deve delegar a maioria do trabalho real para o objeto serviço, lidando com a conversão da interface ou formato dos dados.
- Os **clientes** devem usar o **adaptador** por meio da **interface cliente**. Assim, permite a mudança ou extensão do **adaptador** sem afetar o código **cliente**.

A Figura 3 apresenta a solução arquitetural proposta pelo ***Abstract Factory***.

![Arquitetura do ***Abstract Factory***](../../imagens/criacionais/abstract_factory/abstract_factory_3.png)
**Figura 3:** Arquitetura do padrão ***Abstract Factory***.


```python
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

```

## Exemplo Prático

Considere um exemplo para a execução de músicas em diferentes formatos. Uma solução sem uso de ***Adapter*** é apresentada a seguir:

```python
from abc import ABC, abstractmethod

class Player(ABC):
    
    @abstractmethod
    def play(self, file: str) -> None:
        ...

class MP3Player(Player):

    def play(self, file: str) -> None:
        print(f"Playing MP3: {file}")

class MP4Player:

    def play_mp4(self, file_name: str) -> None:
        print(f"Playing MP3: {file_name}")


def play_audio(player, file) -> None:
    player.play(file)

mp3 = MP3Player()
play_audio(mp3, "music.mp3")

mp4 = MP4Player()
play_audio(mp4, "music.mp4")

```

O exemplo acima apresenta um erro pelo fato do objeto de `MP4Player` não possuir o método `play`.

A aplicação do ***Adapter*** pode ser feita criando uma classe ***Adapter***, que possui como atributo uma instância de ***MP4Player*** e implementa a interface ***Player***. A implementação é apresentada a seguir:

```python
from abc import ABC, abstractmethod

class Player(ABC):
    
    @abstractmethod
    def play(self, file: str) -> None:
        ...

class MP3Player(Player):

    def play(self, file: str) -> None:
        print(f"Playing MP3: {file}")

class MP4Adapter(Player):

    def __init__(self, player: "MP4Player"):
        self.player: "MP4Player" = player

    def play(self, file: str) -> None:
        self.player.play_mp4(file)

class MP4Player:

    def play_mp4(self, file_name: str) -> None:
        print(f"Playing MP4: {file_name}")


def play_audio(player, file) -> None:
    player.play(file)

mp3 = MP3Player()
play_audio(mp3, "music.mp3")

mp4_adapter = MP4Adapter(player=MP4Player())
play_audio(mp4_adapter, "music.mp4")

```

## Aplicabilidade


## Discussão


## Conclusão

