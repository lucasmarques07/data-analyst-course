import pprint

pp = pprint.PrettyPrinter(depth=4)

alunos = {}

qtdTotal = 0 
somaNotas = 0
maiorNota = 0
menorNota = 11
aprovados = 0

while True:

    print('\n1 - Cadatrar Aluno------')
    print('2 - Buscar Aluno--------')
    print('3 - Mostar Todos--------')
    print('4 - Estatísticas--------')
    print('5 - Sair----------------\n')
    opt = int(input('Selecione uma opção: '))

    if opt == 1:

        nome = input('\nDigite um nome (Não pode deixar vazio): ')
        idade = int(input('Digite a idade (Maior que zero): '))
        nota = float(input('Digite a nota (Entre 0 e 10): '))

        if nome == "" or idade <= 0 or nota > 10 or nota < 0: 
            print('\nEntrada inválida!')
        
        elif nome in alunos:
            print('\nEste aluno já está cadastrado! Use outro nome ou adicione um sobrenome.')
        
        else:
            dados_aluno = {
                "Idade": idade,
                "Nota": nota
                }

            alunos[nome] = dados_aluno
            
            print(f'\nAluno {nome} cadastrado!')

            qtdTotal += 1
            
            somaNotas += nota
            
            if nota > maiorNota:
                maiorNota = nota
            
            if nota < menorNota:
                menorNota = nota
            
            if nota > 6:    
                aprovados += 1


    elif opt == 2:
        
        busca = input('\nQual aluno deseja buscar? ')
        
        if busca in alunos:
            print(f'\nDados de {busca}: {alunos[busca]}')
        
        else: 
            print('\nAluno não encontrado!\n')


    elif opt == 3:    
        
        pp.pprint(alunos)

    elif opt == 4:

        print(f'\nA quantidade total de alunos é de: {qtdTotal}')
        print(f'A média das notas dos alunos é de: {somaNotas / len(alunos)}')
        print(f'A maior nota é: {maiorNota}')
        print(f'A menor nota é: {menorNota}')
        print(f'A quantidade de aprovados é de: {aprovados}')
        print(f'A quantidade de reprovados é de: {len(alunos) - aprovados}\n')

    elif opt == 5:
        break    
    else:
        print('\nEntrada inválida!')    

print('\nObrigado por usar o programa!')