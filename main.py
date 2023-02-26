import json

# Conjuntos de operadores
Operators = {'+', '-', '*', '/', '(', ')', '^'}  

# Dicionário contendo a pontuação de prioridades dos operadores
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  

# https://favtutor.com/blogs/infix-to-postfix-conversion#:~:text=How%20to%20Convert%20Infix%20to,match%20the%20order%20of%20operation.

def infixToPostfix(expression):
    stack                   = []  # Declaração de uma "pilha" vazia
    output                  = '' # Declara a saída vazia                                                                                                                                                                                                                    
    step                    = 1
    operation_stack         = ''
    unstaking_operating     = False
    total_output            = dict()
    total_output['steps']   = list()
    steps                   = dict() 

    for character in expression:
        unstaking_operating = False
        operation_stack     = ''
        
        if character not in Operators:  # Se o caracter for um operando já escreve na saída.
            output += character
        elif character == '(':  # Se encontrar abertura: EMPILHA CARACTER
            stack.append('(')
            operation_stack = "Empilhou abertura '('. "
        elif character == ')':  # Se encontrar fechamento: 
                                # DESEMPILHA TODOS CARACTERES EMPILHADOS 
                                # OU ATÉ ENCONTRAR A PRIMEIRA ABERTURA EMPILHADA

            while stack and stack[-1] != '(':
                output              += stack.pop()
                unstaking_operating = True

            if unstaking_operating:
                operation_stack = "Desempilhou até antes da abertura '('. "

            stack.pop() # Desempilha abertura

        else: # OPERADORES MATEMÁTICOS
            
            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()
                unstaking_operating = True
            
            if unstaking_operating:
                operation_stack = 'Desempilhou até acabar a pilha ou até encontrar no topo um operador com prioridade menor. '

            stack.append(character)
            operation_stack += "Empilhou o caracter '" + character + "'. "

        steps['Passo ' + str(step)] = {
                                        'current_token' : character,  
                                        'operation_stack': operation_stack,
                                        'stack_represetation': ''.join(stack),
                                        'postfix_expression': output
                                      }
        step += 1

    unstaking_operating = False
    while stack:
        output += stack.pop()
        unstaking_operating = True
    
    if unstaking_operating:
        steps['Passo ' + str(step)] = {
                                        'current_token' : 'Fim',  
                                        'operation_stack': 'Desempilhou até a pilha ficar vazia. ',
                                        'stack_represetation': ''.join(stack),
                                        'postfix_expression': output
                                    }
    total_output['steps'].append(steps)
    total_output['postfix_expression_final'] = output

    return total_output


if __name__ == '__main__':
    
    print("DIGITE UMA OPÇÃO \n1 - Inserir uma Expressão \n2 - Ler Expressões já existentes no arquivo 'input.txt'\n")
    op = int(input())
    if(op == 1):
        expression = input('Entre com a expressão Infixada: ')
        print('Notação Infixada: ', expression)
        print('Notação Pós-Fixada: ', infixToPostfix(expression))

    elif(op==2):
        file_input_expression = open("input.txt", "r")
        list_file_input = file_input_expression.readlines()
        output_postfix = dict()
        for line in list_file_input:
            expression = line.strip()
            operations_postfix = infixToPostfix(expression)
            output_postfix[expression] = operations_postfix
            print('Notação Infixada: {}Notação Pós-Fixada: {}'.format(line, operations_postfix['postfix_expression_final']))
            print('\n')
        
        with open("output.json", "w", encoding="utf8") as write_file:
            json.dump(output_postfix, write_file, indent = 4, ensure_ascii= False)

        file_input_expression.close()
    else:
        print('Opção Inválida!')
        exit()



