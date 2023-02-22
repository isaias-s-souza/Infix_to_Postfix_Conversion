# Infix_to_Postfix_Conversion

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
    `python main.py`
    
### Logo, você deverá escolher uma das opções abaixo:
    DIGITE UMA OPÇÃO 
    1 - Iserir uma Expressão 
    
        1+2-3
        Notação Infixada: 1+2-3  
        Notação Pós-Fixada: 12+3-
        
    2 - Ler Expressões já existentes no arquivo 'input.txt'
    
        Notação Infixada: 1+2-3  
        Notação Pós-Fixada: 12+3-

        Notação Pós-Fixada: 12+3*

        Notação Infixada: (1+2)*(3-4)
        Notação Pós-Fixada: 12+34-*

        Notação Infixada: 1+((2+3)*(5-6)-7)/(8-9)
        Notação Pós-Fixada: 123+56-*7-89-/+

        Notação Infixada: 1+2*(3+4)-5/6*7+8
        Notação Pós-Fixada: 1234+*+56/7*-8+

    
Referências : https://panda.ime.usp.br/panda/static/pythonds_pt/02-EDBasicos/InfixPrefixandPostfixExpressions.html
