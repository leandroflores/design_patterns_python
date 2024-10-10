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

A Figura 3 apresenta a solução arquitetural proposta pelo ***Abstract Factory***.

![Arquitetura do ***Abstract Factory***](../../imagens/criacionais/abstract_factory/abstract_factory_3.png)
**Figura 3:** Arquitetura do padrão ***Abstract Factory***.


```python


```

## Exemplo Prático


```python



```


## Aplicabilidade


## Discussão


## Conclusão

