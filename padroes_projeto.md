# Padrões de Projeto

Este repositório tem como objetivo apresentar uma visão geral sobre o conceito de **padrões de projeto**. Como fonte principal e as imagens foram retiradas do seguinte endereço: <https://refactoring.guru/pt-br/design-patterns/>.

## Introdução

**Padrões de Projeto** são soluções típicas para problemas comuns em projeto de software. Em outras palavras, um **Padrão de Projeto** é uma solução consolidada e proposta pela comunidade de software para uma situação específica.

No entanto, a utilização de um padrão não consiste simplesmente em copiá-lo para dentro do seu programa, como é feito por bibliotecas e *frameworks*. O padrão não consiste em um trecho de código, mas sim em conceito geral que requer uma **interpretação** e **abstração** para aplicá-lo em seu projeto.

Os **padrões de projeto** costumam ser classificados como sinônimo de **algoritmos**, no entanto, tal associação é equivocada. Um algoritmo corresponde à um conjunto de ações determinadas (nível mais baixo de abstração), enquanto que um padrão é uma descrição de solução (alto nível de abstração). Assim, um mesmo padrão pode resultar em algoritmos bem diferentes.

## Definição Formal

Os **Padrões de Projeto** são compostos de uma descrição formal que deve ser abstraída para a aplicação no contexto da aplicação alvo. A descrição de um padrão normalmente possui:

* **Propósito:** contextualização do problema e apresentação de uma solução.
* **Motivação:** descrição minuciosa do problema e a solução que o padrão propõe.
* **Estrutura:** apresentação das classes e seus relacionamentos que definem o padrão.

A definição formal de um padrão podem incluir ainda aplicabilidade, etapas de implementação e relação com outros padrões. No entanto, a forma mais efetiva de compreender um padrão é por meio de exemplos de código em cenários reais.

## Histórico

Os **padrões de projeto** foram soluções propostas para problemas recorrentes em projetos orientados a objetos. Em resumo, os padrões foram propostas a medida que se identificaram problemas comuns de arquitetura de software em contextos completamente distintos.

O conceito padrões foi primeiramente descrito por Christopher Alexander em seu livro `A Pattern Language` em 1977. O livro apresenta uma linguagem de padrões para o projeto de um ambiente urbano.

Para o contexto de software, o conceito de padrões foi introduzido por Erich Gamma, John Vlissides, Ralph Johnson e Richard Helm, na publicação de `Design Patterns: Elements of Reusable Object-Oriented Software` em outubro de 1994. O livro apresenta 23 padrões para problemas distintos em projetos orientado a objetos. A publicação foi um sucesso, passando a ser conhecido como "o livro da Gangue dos Quatro (*Gang of Four*)", sendo abreviado para o "livro do GoF".

A abordagem de padrões tornou-se popular e reconhecida no meio acadêmico e industrial, sendo extendidos para diferentes paradigmas, com a apresentação e discussão de novos padrões.

## Motivação

Para um programador, a motivação para estudar e compreender **padrões de projeto** é passar a ampliar o domínio em soluções possíveis em problemas recorrentes ao paradigma de orientação a objetos.

Provavelmente, muitos programadores trabalhem por longo tempo sem saber formalmente nada sobre padrões, mesmo implementando alguns padrões sem nem saber.

Portanto, a motivação para o aprendizado é o conhecimento de **soluções** propostas e testadas para problemas comuns de projeto de software. Além do fato do aprendizado em uma linguagem comum que pode ser abstraída e aplicada em softwares escritos em linguagens de programação distintas.

Alguns argumentos contra os padrões de projeto foram apresentados, incluindo contorno para linguagens de programação ineficientes, soluções ineficientes e dogmáticas e uso repetitivo e injustificável. A discussão é pertinente, e como qualquer conceito, o uso de padrões deve ser discutido e adptado ao contexto do problema identificado.

## Classificação dos Padrões

Os padrões de projeto se diferenciam por complexidade, detalhamento e aplicabilidade ao sistema.

Uma classificação possível é em relação ao nível:

* **Idiomáticos:** mais básicos (baixo nível), sendo aplicados à uma única linguagem de programação.
* **Arquitetônicos:** mais universais (alto nível), sendo aplicados em qualquer linguagem de programação pelo fato da definição ser na arquitetura do sistema.

A classificação mais conhecida é referente ao propósito, sendo possível observar três categorias:

* **Padrões Criacionais:** fornecem mecanismos para a **criação** de objetos que aumentam a flexibilidade e reutilização de código.
* **Padrões Estruturais:** explicam como montar objetos e classes em **estruturas**, mantendo as estruturas flexíveis e eficientes.
* **Padrões Comportamentais:** cuidam da **comunicação** eficiente e da assinalação de responsabilidades entre objetos.

### Padrões Criacionais

Os **padrões criacionais** fornecem mecanismos de **criação** de objetos, que aumentam a flexibilidade e reutilização de código. Existem cinco padrões classificados como criacionais: *Factory Method*, *Abstract Factory*, *Builder*, *Prototype* e *Singleton*.

### Padrões Estruturais

Os **padrões estruturais** explicam como montar objetos e classes em estruturas maiores, mas ainda mantendo essas estruturas flexíveis e eficientes. Existem sete padrões classificados como estruturais: *Adpter*, *Bridge*, *Composite*, *Decorator*, *Facade*, *Flyweight* e *Proxy*

### Padrões Comportamentais

Os **padrões comportamentais** são voltados aos algoritmos e a designação de responsabilidade entre objetos. Existem dez padrões que são classificados como comportamentais: *Chain of Responsability*, *Command*, *Iterator*, *Mediator*, *Memento*, *Observer*, *State*, *Strategy*, *Template Method* e *Visitor*.
