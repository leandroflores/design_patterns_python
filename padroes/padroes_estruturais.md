# Padrões Estruturais

Os **padrões estruturais** explicam como montar objetos e classes em estruturas maiores, mas ainda mantendo essas estruturas flexíveis e eficientes. Existem sete padrões classificados como estruturais: ***Adapter***, ***Bridge***, ***Composite***, ***Decorator***, ***Facade***, ***Flyweight*** e ***Proxy***.

## Adapter

O ***Adapter*** é um padrão de projeto estrutural que permite a colaboração de objetos incompatíveis. O padrão ***Adapter*** atua como um *wrapper* entre dois objetos, capturando chamadas para um objeto e as deixa reconhecíveis como interface para o segundo objeto.

A Figura 1 apresenta o diagrama com a solução do padrão ***Adapter***.

![Adapter](../imagens/estruturais/adapter/adapter_.png)
**Figura 1:** Arquitetura do padrão ***Adapter***.

## Bridge

O ***Bridge*** é um padrão de porjeto estrutural que divide a lógica do negócio em hierarquias de classe separadas que podem ser desenvolvidas independentemente.

Uma dessas hierarquias (**Abstração**) obterá uma referência à um objeto da segunda hierarquia (**Implementação**). A **abstração** poderá delegar chamadas para o objeto de **implementações**. Como todas as implementações possuem uma interface comum, são intercambiáveis dentro da abstração.

A Figura 2 apresenta o diagrama com a solução do padrão ***Bridge***.

![Bridge](../imagens/estruturais/bridge/bridge_.png)
**Figura 2:** Arquitetura do padrão ***Bridge***.

## Composite

O ***Composite*** é um padrão de projeto estrutural que permite compor objetos em uma estrutura semelhante à uma árvore e trabalhar com eles como se fosse um objeto singular.

O padrão ***Composite*** se tornou uma solução bastante popular para a maioria dos problemas que exigem a consutrução de uma estrutura em árvore. O grande recurso do ***Composite*** é a capacidade de executar métodos recursivamente em toda a estrutura de árvore e resumir os resultados.

A Figura 3 apresenta o diagrama com a solução do padrão ***Composite***.

![Composite](../imagens/estruturais/composite/composite_.png)

**Figura 3:** Arquitetura do padrão ***Composite***.

## Decorator

O ***Decorator*** é um padrão de projeto estrutural que permite adicionar novos comportamentos aos objetos dinamicamente, colocando-os dentro de objetos *wrapper* especiais.

O padrão ***Decorator*** permite o agrupamento de objetos inúmeras vezes, pelo fato dos objetos de destino e os decoradores implementarem a mesma interface. O objeto resultante terá um comportamento de empilhamento de todos os *wrappers*.

A Figura 4 apresenta o diagrama com a solução do padrão ***Decorator***.

![Decorator](../imagens/estruturais/decorator/decorator_.png)

**Figura 4:** Arquitetura do padrão ***Decorator***.

## Facade

O ***Facade*** é um padrão de projeto estrutural que fornece uma interface simplificada para um sistema complexo de classes, biblioteca ou *framework*. Embora o padrão ***Facade*** diminua a complexidade geral, também ajuda a centralizar dependências indesejadas em um único local.

A Figura 5 apresenta o diagrama com a solução do padrão ***Facade***.

![Facade](../imagens/estruturais/facade/facade_.png)

**Figura 5:** Arquitetura do padrão ***Facade***.

## Flyweight

O ***Flyweight*** é um padrão de projeto estrutural que permite que os programas suportem grandes quantidades de objetos, mantendo baixo consumo de memória. O padrão consegue por meio do compartilhamento de partes do estado do obejeto entre vários objetos. Em outras palavras, o padrão ***Flyweight*** economiza RAM armazenando em *cache* os mesmos dados usados por objetos diferentes.

A Figura 6 apresenta o diagrama com a solução do padrão ***Flyweight***.

![Flyweight](../imagens/estruturais/flyweight/flyweight_.png)

**Figura 6:** Arquitetura do padrão ***Flyweight***.

## Proxy

A Figura 7 apresenta o diagrama com a solução do padrão ***Proxy***.


![Proxy](../imagens/estruturais/proxy/proxy_.png)

**Figura 7:** Arquitetura do padrão ***Proxy***.
