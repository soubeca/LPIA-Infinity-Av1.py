qtd_studant = int(input('Informe a quantidade de alunos: '))
#Armazena a média dos alunos
n_general = 0

for i in range(1,qtd_studant):
    name = str(input(f'Qual o nome do {i}º aluno? '))
    n1 = float(input('Informe  a 1º nota:'))
    n2 = float(input('Informe  a 2º nota:'))
    n3 = float(input('Informe  a 3º nota:'))
    
    #Calcula a média do aluno fornecidos
    average = (n1 + n2 + n3) / 3
    #Adiciona a média do aluno na variável, cada média coletada é somada com a anterior
    n_general += average
    #Divide a média geral somada pela quantidade de alunos
    general_average = n_general / qtd_studant
    
    if average >= 7:
        print(f'✅ {name} foi APROVADO com a média {average:.1f}')
        print(f' 1º Nota = {n1:.1f}')
        print(f' 2º Nota = {n2:.1f}')
        print(f' 3º Nota = {n3:.1f}')
    else:
        print(f'❌ {name} foi REPROVADO com a média {average:.1f}')
        print(f' 1º Nota = {n1:.1f}')
        print(f' 2º Nota = {n2:.1f}')
        print(f' 3º Nota = {n3:.1f}')

print(f'A média geral da turma é de {general_average:.1f}')
