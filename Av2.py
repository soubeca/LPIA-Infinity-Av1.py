#Crie um programa em Python para verificar se um número é positivo, negativo ou zero. 
# O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.
#Se o número for maior que zero, exiba a mensagem "O número é positivo." Se for menor que zero, exiba "O número é negativo."
#Caso seja zero, a mensagem deve ser "O número é zero."
#Utilize estruturas condicionais e formatação com F-string para criar o programa de forma clara.


number = int(input('Insira um número inteiro: '))

if number > 0:
    print(f'O número {number} é positivo!')
elif number < 0:
    print(f'O número {number} é negativo!')
else:
    print(f'O número é {number}.')
