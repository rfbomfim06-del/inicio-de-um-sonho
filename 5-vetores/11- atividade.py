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
                print('o nome do jogador deve ser inserido...')
            else:
                lista_jogadores.append(nome_jogador)
                print('jogador cadastrado com sucesso!')
        case 2:
            print('== LISTA DOS jogador ==')
            for jogador in lista_jogadores:
                print(f'- {jogador}')
            print(f'Total:{len(lista_jogadores)}')
        case 3:
            print('=== ATUALIZAR JOGADOR ==')
            nome = input('qual jogador deseja atualizar? ').strip().upper()
            if nome in lista_jogadores:
                posicao = lista_jogadores.index(nome)
                novo = input('novo nome: ').strip().upper()
                lista_jogadores[posicao] = novo
                print('jogador alterado com sucesso')
            else:
                print(' jogador nao encontrado.')
        case 4:
            #DELETE(REMOVER)
            print('=== REMOVER jogador ==')
            nome = input('qual jogador deseja remover? ').strip().upper()
            if nome in lista_jogadores:
                lista_jogadores.remove(nome)
                print('jogador excluido sucesso')
            else:
                print(' jogador nao encontrado.')
        case 5:
            #READ(LER / CONSULTA / BUSCAR)
            print('=== ENCONTRAR jogador ==')
            nome = input('qual jogador deseja encontrar? ').strip().upper()
            if nome in lista_jogadores:
                print('jogador encontrado')
            else:
                print(' jogador nao esta no sistema.')
            

        case 0:
            print('Saindo do programa.....')
            break
        case _:
            print('\nOpção inválida! \nTente novamente....')

    input('Pressione uma tecla para continuar....').strip().upper()
    os.system('cls')
