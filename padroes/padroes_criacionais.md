# Padrões Criacionais

Os **padrões criacionais** fornecem mecanismos de **criação** de objetos, que aumentam a flexibilidade e reutilização de código. Existem cinco padrões classificados como criacionais: *Factory Method*, *Abstract Factory*, *Builder*, *Prototype* e *Singleton*.

## Singleton

O ***Singleton*** é um padrão de projeto criacional que garante uma instância única para a classe, fornecendo um ponto de acesso único à instância no sistema.

A Figura 1 apresenta o diagrama com a solução do padrão ***Singleton***.

<html>
<img src="../imagens/criacional/singleton/singleton_3.png" width="350" alt="Singleton">
<p><b>Figura 1</b>: Diagrama com a definição do <i>Singleton</i>.</p>
</html>

A classe ***Singleton*** declara o método estático que retorna sempre a instância única. O construtor deve ser privado para não ser chamado diretamente pelo **Cliente**. O acesso ao objeto só é possível pelo método estático.

## Prototype

O ***Prototype*** é um padrão de projeto criacional que permite a **clonagem** de objetos, mesmo complexos, sem acoplamento à suas classes específicas.

A Figura 2 apresenta o diagrama com a solução do padrão ***Prototype***.

<html>
<img src="../imagens/criacional/prototype/prototype_2.png" width="400" alt="Prototype">
<p><b>Figura 2</b>: Diagrama com a definição do <i>Prototype</i>.</p>
</html>

A interface ***Prototype*** declara os métodos de clonagem. A classe **Protótipo Concreta** implementa o método de clonagem. Além da cópia dos atributos do objeto original, pode incluir a cópia específica de outros objetos relacionados. O **Cliente** pode produzir uma cópia de qualquer objeto que implementa a interface do **Protótipo**.

## Factory Method

O ***Factory Method*** um padrão de projeto criacional, que resolve o problema de criar objetos de produtos sem especificar suas classes concretas. O ***Factory Method*** define um método, que deve ser usado para criar objetos em vez da chamada direta ao construtor.

A Figura 3 apresenta a arquitetura proposta pelo ***Factory Method***:

<html>
<img src="../imagens/criacional/factory_method/factory_method_2.png" width="400" alt="Factory Method">
<p><b>Figura 3</b>: Diagrama com a definição do <i>Factory Method</i>.</p>
</html>

O ***Factory Method*** é definido por um **método fábrica** para a instanciação de objetos ao invés de chamadas diretas para os construtores.

## Builder

O ***Builder*** é um padrão de projeto criacional, que permite a construção de objetos complexos passo a passo. O ***Builder*** não exige que os produtos tenham uma interface comum. Isso torna possível produzir produtos diferentes usando o mesmo processo de construção.

A Figura 4 apresenta o diagrama com a solução do padrão ***Builder***.

<html>
<img src="../imagens/criacional/builder/builder_2.png" width="400" alt="Builder">
<p><b>Figura 4</b>: Diagrama com a definição do <i>Builder</i>.</p>
</html>

A interface ***Builder*** deve declarar as etapas de construção do produto, que são comuns a todos os tipos de ***buiders***. ***Builders* Concretos** fornecem diferentes implementações para as etapas de construção. ***Builders* Concretos** podem produzir produtos que não seguem a interface em comum.

**Produtos** são os objetos resultantes dos ***builders* concretos**. Os **Produtos** construídos por diferentes ***builders*** não precisam pertencer à mesma interface ou hierarquia de classe.

A **Classe Diretor** define a ordem na qual as etapas da construção são chamadas. É possível criar e reutilizar configurações específicas de produtos. O **Cliente** deve associar um dos ***builders*** com a **Classe Diretor**. Normalmente, é feito por meio dos parâmetros do construtor do diretor, existindo um único ***builder*** para todas as construções. 

## Abstract Factory

O ***Abstract Factory*** é um padrão de projeto criacional, que apresenta uma solução para criar famílias inteiras de produtos sem especificar suas classes concretas.

A Figura 5 apresenta a solução arquitetural proposta pelo ***Abstract Factory***.

<html>
<img src="../imagens/criacional/abstract_factory/abstract_factory_3.png" width="400" alt="Abstract Factory">
<p><b>Figura 5</b>: Arquitetura do <i>Abstract Factory</i>.</p>
</html>


Neste cenário, apesar das **fábricas concretas** retornarem produtos concretos, as assinaturas dos métodos retornar um tipo abstrato de produtos. Assim, o código cliente não fica ligado à uma variante específica, mas a qualquer variante do respectivo produto.
