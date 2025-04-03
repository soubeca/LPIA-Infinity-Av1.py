# Você está criando um programa em Python para simular um jogo simples de adivinhação.
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar.
# O jogador terá até 3 tentativas para acertar o número.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. 
# Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

numberSecret = 9
attempt = 3
playerAttempt = 0

while True:
    print(':::::::💣 DESCUBRA O NÚMERO SECRETO 💣:::::::::')
    playerNumber = int(input('Informe um número: '))
    playerAttempt += 1
    
    if playerNumber == numberSecret:
        print('🎉 PARABÉNS, VOCÊ ACERTOU! 🎉')
        print(f'O número secreto é {numberSecret}.')
        break
    elif playerAttempt == attempt:
        print('Que pena, suas chances acabaram!😥')
        break
    else:
        print('Não foi dessa vez, mas você ainda pode tentar!')
