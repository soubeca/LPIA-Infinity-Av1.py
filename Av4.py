# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. 
# Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
# Ao final, exiba a soma dos números pares encontrados.

number1 = int(input('Digite o número que irá iniciar: '))
number2 = int(input('Digite o número que irá finalizar:'))
sum = 0

for i in range(number1, number2):
    if i %2 == 0:
        sum += i
        print({i})
    else:
        print(f'O número {i} é impar!')
        
print(f'A soma dos números pares é igual a {sum}')
