# *Singleton*

O ***Singleton*** é um padrão de projeto classificado como **criacional**.

**Propósito**: garantir que uma classe tenha **apenas** uma **instância**, enquanto fornece um ponto de acesso global para essa instância.

**Problema**: o ***Singleton*** resolve dois problemas de uma só vez, violando o **princípio de responsabilidade única**:

- Garantir que uma classe tenha uma única instância. A razão mais comum para controlar o número de instâncias deve-se ao acesso a algum recurso compartilhado (exemplo banco de dados ou arquivo).

A lógica consiste em ao invés de criar um novo objeto, obter o objeto já criado anteriormente. Este comportamento é impossível de implementar com um construtor regular, pelo fato de todo construtor retornar sempre uma nova instância.

- Fornecer um ponto de acesso global para a instância. No caso de variáveis globais, existe a insegurança de qualquer código poder potencialmente sobrescrever conteúdos da instância global.

Assim como uma variável global, o padrão ***Singleton*** permite acesso de qualquer lugar do programa. No entanto, a instância é protegida de sobrescrita por outro código.

**Solução**: todas as soluções ***singleton*** possuem dois passos em comum:

- **Construtor privado** para prevenir que de outros lugares usem o operador ***new*** com a classe ***singleton***.
- **Método estático** agindo como um construtor, sendo responsável por chamar o construtor privado e salvá-lo em um campo estático, sendo que todas as chamadas desse método retornam o objeto em *cache*.

Portanto, todo lugar que possua acesso à classe ***singleton***, será capaz de chamar o **método estático**, recebendo o objeto armazenado em *cache*.

**Exemplo**: um país pode possuir apenas um governo oficial. Independente das identidades pessoais dos indivíduos que formam os governos, o título, "O Governo de X", é um ponto de acesso global que identifica o grupo de pessoas.

**Estrutura**: a classe ***Singleton*** declara o método estático ***getInstance*** que retorna a mesma instância de sua própria classe. O construtor da classe ***Singleton*** deve ser escondido do código cliente. Chamando o método ***getInstance*** deve ser o único modo de obter o objeto ***singleton***.

## Aplicabilidade

O padrão ***singleton*** deve ser aplicado quando uma classe em seu programa deve ter apenas uma instância disponível para todos os seus clientes.

O padrão ***singleton*** desabilita todos os meios de criar objetos de uma classe exceto pelo método especial de criação. Este método pode criar um novo objeto ou retornar um objeto existente caso já tenha sido criado.

O padrão ***singleton*** é recomendado para o controle mais estrito de variáveis globais.

Ao contrário das variáveis globais, o padrão ***singleton*** garante que existe apenas uma instância da classe. Apenas a própria classe ***singleton*** pode substituir a instância salva em *cache*.

Caso seja necessário permitir a criação de várias instâncias, o único trecho de código necessário para mudanças é o método ***getInstance***.

## Implementação

- Adicione um campo privado estático na classe para o armazenamento da instância ***singleton***.
- Declare um método de criação público estático para obter a instância ***singleton***.
- Implemente a "inicialização preguiçosa" dentro do método estático, que deve criar um novo objeto na primeira chamada e armazená-lo em um campo estático. Assim, o método deve sempre retornar esta instância em todas as próximas chamadas.
- Deixe o construtor da classe privado. O método estático da classe vai ainda ser capaz de chamar o construtor, mas não os demais objetos.
- Encontre todas as chamadas diretas para o construtor do ***singleton*** para o método de criação estático.

## Discussão

- Pontos Positivos:
  - Certeza que uma classe terá somente uma única instância.
  - Ponto de acesso global para a instância.
  - Objeto inicializado somente na primeira chamada do método.

- Pontos Negativos:
  - Não segue o princípio de responsabilidade única, resolvendo dois problemas de uma vez.
  - Pode mascarar um *design* ineficiente, quando os componentes do programa sabem muito sobre cada um.
  - Requer tratamento especial em um ambiente *multithreaded* para que múltiplas *threads* não possam criar vários objetos.
  - Dificuldade em fazer testes unitários.
