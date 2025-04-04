# Crie um programa em Python que simule um sistema de login. 
# O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

user = 'rebeca.souza'
password = 'JesuSalva'

qtd_attempt = 3

for i in range (1,4):
  
  name_user = str(input('Insira o seu usuário: '))
  password_user = str(input('Insira sua senha: '))
  
  if name_user == user and password_user == password:
    print('☺️ Bem-Vindo(a) a nossa central de atendimento!')
    break
  elif i == 3:
    print('🚫 Acesso BLOQUEADO! Você excedeu o limite de tentativas')
  else:
    qtd_attempt -= 1
    print(f'Credenciais inválidas! Restam {qtd_attempt} tentativas.')
  
