import os
os.system('cls')

lista_jogadores = []

while True:

    print('''
== BARCELONA FC ==
1 - cadastrar jogador
2 - listar jogador
3 - atualizar jogador
4 - dispensar jogador
''')

    codigo = int(input('digite o codigo: '))

    match codigo:
        case 1:
            #CREATE (INSERIR)
            print('== CADASTRAR jogador ==')
            nome_jogador = input('Digite o nome do novo jogador: ').strip().upper()
            posicao_jogador = input('Digite a posiçao do jogador: ').strip().upper()
            camisa_jogador = int(input('Digite a sua camisa do jogador: '))
            if nome_jogador == '':
                print('o nome do joador deve ser inserido...')
            else:
                lista_jogadores.append(nome_jogador)
                print('Produto cadastrado com sucesso!')
        case 2:
            print('== LISTA DOS PACIENTES ==')
            for paciente in lista_jogadores:
                print(f'- {paciente}')
            print(f'Total:{len(lista_jogadores)}')
        case 3:
            print('=== ATUALIZAR JOGADOR ==')
            nome = input('qual paciente deseja atualizar? ').strip().upper()
            if nome in lista_jogadores:
                posicao = lista_jogadores.index(nome)
                novo = input('novo nome: ').strip().upper()
                lista_jogadores[posicao] = novo
                print('paciente alterado com sucesso')
            else:
                print(' protudo nao encontrado.')

