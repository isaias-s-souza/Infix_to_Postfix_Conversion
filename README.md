# Infix_to_Postfix_Conversion

## Passo a passo resumido.
    - Leu um operando. Escreve na saída
    - Leu abertura de parênteses. Empilha.
    - Leu fechamento de parênteses. Desempilha escrevendo na saída até encontrar a abertura de parênteses correspondente. Desempilha abertura correspondente sem escrita na saída.
    - Leu operador, verifica o topo da pilha e faz a comparação entre os dois, desempilhando e escrevendo na saída até esvaziar a pilha caso o operador atualmente lido for de menor prioridade que o topo em cada nova comparação após o desempilhamento. Se o operador lido for de maior prioridade que o topo da pilha, somente será empilhado.
    - Após a leitura de todos caracteres da expressão será desempilhado todos operadores da pilha.
## Defifinição de Expressões Infixadas e Pós-Fixadas

### Infixada
    Diz respeito aos operadores " +,-,*,/ " inseridos entre as expressões.
    Ex.: A + B * C, onde as variáveis A, B e C estão sendo manipuladas pelos operadores(DE ACORDO COM SUAS PRIORIDADES)

### Pre-Fixada
    Diz respeito aos operadores " +,-,*,/ " inseridos antes das expressões.
    Ex.: +A*BC, onde as variáveis A, B e C estão sendo manipuladas pelos operadores(DE ACORDO COM SUAS PRIORIDADES)

### Pós-Fixada
    Diz respeito aos operadores " +,-,*,/ " inseridos depois das expressões.
    Ex.: ABC*+ , onde as variáveis A, B e C estão sendo manipuladas pelos operadores(DE ACORDO COM SUAS PRIORIDADES)

### Para executar basta rodar o arquivo(com o python instalado) `main.py` em seu terminal
    python main.py
    
### Logo, você deverá escolher uma das opções abaixo:
    DIGITE UMA OPÇÃO 
    1 - Inserir uma Expressão 
    
        1+2-3
        Notação Infixada: 1+2-3  
        Notação Pós-Fixada: 12+3-
        
    2 - Ler Expressões já existentes no arquivo `input.txt`
    
        Notação Infixada: 1+2-3
        Notação Pós-Fixada: 12+3-


        Notação Infixada: (1+2)*3
        Notação Pós-Fixada: 12+3*


        Notação Infixada: (1+2)*(3-4)
        Notação Pós-Fixada: 12+34-*


        Notação Infixada: 1+((2+3)*(5-6)-7)/(8-9)
        Notação Pós-Fixada: 123+56-*7-89-/+


        Notação Infixada: 1+2*(3+4)-5/6*7+8
        Notação Pós-Fixada: 1234+*+56/7*-8+

### Com isso, além de imprimir na tela, será também gerado um arquivo `output.json` que faz um detalhamento das operações com cada expressão de entrada. 
    
Referências : https://panda.ime.usp.br/panda/static/pythonds_pt/02-EDBasicos/InfixPrefixandPostfixExpressions.html
