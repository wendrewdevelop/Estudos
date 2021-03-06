## Analise Léxica ##

1. A primeira etapa lê a entrada de caracteres, um de cada vez, mudando o estado em que os caracteres se encontram. Quando o analisador encontra um caractere que ele não identifica como correto, ele o chama de "estado morto" então, ele volta à última análise que foi aceita e assim tem o tipo e comprimento do léxico válido. Um léxico, entretanto, é uma única lista de caracteres conhecidas de ser um tipo correto. Para construir um símbolo, o analisador léxico necessita de um segundo estado. 
<br>
2. Nesta etapa são repassados os caracteres do léxico para produzir um valor. O tipo do léxico combinado com seu valor é o que adequadamente constitui um símbolo, que pode ser dado a um parser. (Alguns símbolos tais como parênteses não têm valores, e então a função da análise não pode retornar nada). A análise léxica escreve um parser muito mais fácil. Em vez de ter que acumular, renomeia seus caracteres individualmente. O parser não mais se preocupa com símbolos e passa a preocupar-se só com questões de sintática. Isto leva a eficiência de programação, e não eficiência de execução. Entretanto, desde que o analisador léxico é o subsistema que deve examinar cada caractere único de entrada, podem ser passos intensivos e o desempenhos se torna crítico, pode estar usando um compilador.


## TODO ##

- [ ] Obter uma lista de caracteres e separar caracter por caracter

- [x] Implementar As classes na resposta do codigo

- [ ] Implementar As classes na execução do codigo