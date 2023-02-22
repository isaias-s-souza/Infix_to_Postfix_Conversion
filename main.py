import os

Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators

# https://favtutor.com/blogs/infix-to-postfix-conversion#:~:text=How%20to%20Convert%20Infix%20to,match%20the%20order%20of%20operation.

def infixToPostfix(expression):
    stack = []  # initialization of empty stack

    output = ''

    for character in expression:

        if character not in Operators and character.isdigit():  # if an operand append in postfix expression

            output += character

        elif character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:
            
            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output += stack.pop()

    return output


if __name__ == '__main__':
    
    print("DIGITE UMA OPÇÃO \n1 - Iserir uma Expressão \n2 - Ler Expressões já existentes no arquivo 'input.txt'\n")
    op = int(input())
    if(op == 1):
        expression = input('Entre com a expressão Infixada: ')
        print('Notação Infixada: ', expression)
        print('Notação Pós-Fixada: ', infixToPostfix(expression))

    elif(op==2):
        file_input_expression = open("input.txt", "r")
        list_file_input = file_input_expression.readlines()

        for line in list_file_input:
            print('Notação Infixada: {}Notação Pós-Fixada: {}'.format(line, infixToPostfix(line.strip())))
            print('\n')
        file_input_expression.close()
    else:
        print('Opção Inválida!')
        exit()



