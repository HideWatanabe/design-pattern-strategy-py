# Strategy

## Definição do GoF, no livro "Padrões de Projeto" (2000)

### Intenção: 
Definir uma família de algoritmos, encapsular cada uma delas e torná-las intercambiáveis. **Strategy** permite que o 
algoritmo varie independentemente dos clientes que o utilizam.

### Tipo de pattern:
Comportamental

### Também conhecido como:
Policy

### Aplicável quando:
- Muitas classes relacionadas diferem somente no seu comportamento. As estratégias fornecem uma maneira de configurar
uma classe com um dentre muitos comportamentos.
- Você necessita de variantes de um algoritmo. Por exemplo, pode definir algoritmos que refletem diferentes soluções de 
compromisso entre espaço/tempo. As estratégias podem ser usadas quando essas variantes são implementadas como uma 
hierarquia de classes de algoritmos.
- Um algoritmo usa dados dos quais os clientes não deveriam ter conhecimento. Use o padrão **Strategy** para evitar a 
exposição das estruturas de dados complexas, específicas de cada algoritmo.
- Uma classe define muitos comportamentos, e esses aparecem em suas operações como múltiplos comandos condicionais da 
linguagem. Em vez de usar muitos comandos condicionais, mova os ramos condicionais relacionados para a sua própria
classe **Strategy**

### Participantes:
- **Strategy:** Define uma interface comum para todos os algoritmos suportados. **Context** usa essa interface para
chamar o algoritmo definido por uma **ConcreteStrategy**.
- **ConcreteStrategy:** Implementa o algoritmo usando a interface de **Strategy**
- **Context:** É configurado com um objeto **ConcreteStrategy**. Mantém uma referência para um objeto **Strategy**. 
Pode definir uma interface que permite que **Strategy** acesse seus dados. 