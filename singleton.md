# *Singleton*

O ***Singleton*** é um padrão de projeto classificado como **criacional**.

**Propósito**: garantir que uma classe tenha **apenas** uma **instância**, enquanto fornece um ponto de acesso global para essa instância.

**Problema**: o ***Singleton*** resolve dois problemas de uma só vez, violando o **princípio de responsabilidade única**:

- Garantir que uma classe tenha uma única instância. A razão mais comum para controlar o número de instâncias deve-se ao acesso a algum recurso compartilhado (exemplo banco de dados ou arquivo).

A lógica consiste em ao invés de criar um novo objeto, obter o objeto já criado anteriormente. Este comportamento é impossível de implementar com um construtor regular, pelo fato de todo construtor retornar sempre uma nova instância.

- Fornecer um ponto de acesso global para a instância. No caso de variáveis globais, existe a insegurança de qualquer código poder potencialmente sobrescrever conteúdos da instância global.

Assim como uma variável global, o padrão ***Singleton*** permite acesso de qualquer lugar do programa. No entanto, a instância é protegida de sobrescrita por outro código.
