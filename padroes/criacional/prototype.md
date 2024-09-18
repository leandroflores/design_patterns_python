# Prototype

## Propósito

O ***Prototype*** é um **padrão de projeto criacional** que permite copiar objetos existentes sem fazer seu código ficar dependente de suas classes.

## Problema

Considere a necessidade de criar a cópia exata de um objeto. O primeiro passo é criar um novo objeto da mesma classe. Posteriormente, passar por todos os atributos do objeto original e copiar seus valores para o novo objeto.

Porém, considere o cenário de atributos privados, em que não é possível acessá-los fora do escopo do próprio objeto.

<html>
<img src="../../imagens/criacional/prototype/prototype_1.png" width="400" alt="Factory Method">
<p><b>Figura 1</b>: Representação de diferentes combinações possíveis para uma casa.</p>
</html>

Outro problema é que a necessidade de saber exatamente a classe do objeto original para criar uma cópia, configura uma dependência. Em casos que a dependência segue o tipo de uma interface, é impossível saber a classe exatamente.

## Solução

O padrão ***Prototype*** transmite o processo de cópia para o próprio objeto a ser clonado. O padrão declara uma interface comum para todas as classes que podem ter objetos a ser clonados. Essa interface permite a chamada do método que faz a cópia, sem acoplar seu código à classe do objeto. Normalmente, a interface possui um único método: `clonar`.

A implementação do método `clonar` é muito parecida em todas as classes. O método cria um objeto da classe atual e carrega todos os valores dos atributos para o novo objeto, incluindo os atributos privados da classe. Um objeto que suporta clonagem é chamado de **protótipo**. Para objetos extensos, com muitos atributos, torná-lo um **protótipo** é uma alternativa adequada.


## Implementação

A implementação do ***Prototype*** não é definida por um algoritmo, mas pode ser descrita por alguns passos:
- Crie uma interface protótipo e declare o método `clonar`.


A Figura 2 apresenta o diagrama com a solução do padrão ***Builder***.

<!-- <html>
<img src="../../imagens/criacional/builder/builder_2.png" width="400" alt="Builder">
<p><b>Figura 2</b>: Diagrama com a definição do <i>Builder</i>.</p>
</html> -->


A implementação em Python segue abaixo:

```python


```

## Exemplo Prático

```python


```

O exemplo a seguir apresenta a refatoração com o padrão ***Prototype***:

```python


```



## Conclusão

