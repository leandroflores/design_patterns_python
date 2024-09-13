# Factory Method

## Propósito

O ***Factory Method*** (método fábrica) é um **padrão de projeto criacional** que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

## Problema

Considere o seguinte cenário: existe uma aplicação de logística criada que lida com apenas o transporte por caminhões. A maior parte do código fica na classe `Caminhão`. A aplicação fica popular e passa a ser requisitada para a logística marítima.

A maior parte do código é altamente acoplada à classe `Caminhão`. Adicionar a classe `Navio` exige alteração em toda a base do código. Além disso, para todo eventual novo meio de transporte é necessário fazer alterações novamente.

Como resultado, o código-fonte fica sujo, repleto de condicionais que alteram o fluxo de execução, dependendo da classe de objetos de transporte.

## Solução

O padrão ***Factory Abstract*** apresenta como solução a alteração das chamadas diretas para construtores para chamadas de um método da **fábrica** especial. Os objetos ainda são criados com construtores, que são invocados dentro do método da **fábrica**. Os **objetos** retornados pelo **método** da **fábrica** são chamados de **produtos**.

Em um primeiro momento, tal mudança parece pouco justificável, pelo fato de apenas mudar a chamado do construtor para outra parte do código. No entanto, é possível sobrescrever o método fábrica em uma subclasse e alterar a classe de produtos que estão sendo instanciados.

Porém, existe uma limitação: só é possível retornar tipos diferentes de produtos no caso de ser usado uma classe ou interface comum. Além disso, o tipo de retorno deve seguir exatamente a assinatura do método declarado na **fábrica**.

No exemplo de logística, uma refatoração seria com as classes `Caminhão` e `Navio` implementando a interface `Transporte`, que define o método abstrato `transportar`. Cada classe implemente o método de acordo com sua regra de negócio própria.

A imagem a seguir apresenta a arquitetura apresentada para a solução:

<figure>
    <img src="../../imagens/criacional/factory_method.png" alt="Logo do Ubuntu" width="400">
    <figcaption><b>Figura 1</b>: Arquitetura da solução para o <i>Template Method</i>.</figcaption>
</figure>
