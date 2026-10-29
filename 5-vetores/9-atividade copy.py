import os
os.system('cls')

lista_filmes = []

while True:
    print('''
    === FILMES ===
    1-Cadastrar filme
    2- listar de filme
    0- sair
    ''')

    opcao = int(input('escolha uma opção: '))

    match opcao:
        case 1:
            print('\n == CADASTRAR O FILME ==')
            #strip()retira os espaços vazios no final.
            #upper() todas as letras maiusculas.
            nome = input('nome do novo filme: ').strip().upper()

            if nome == '':
                print('O nome não pode ficar vazio. ')
            elif nome in lista_produtos:
                print(f'{nome} ja está cadastrado. ')
            else:
                # .append(nome) adiciona o nome do produto na lista.
                lista_produtos.append(nome)
                print('produto cadaastrado com sucesso! ')
            input( '\n pressione uma tecla para continuar...')

        case 2:
            print('\n == LITRAR TODOS OS FILMES ==')
            if len(lista_produtos) == 0:
                print('O estoque esta vazio')
            else:
                for i, produto in enumerate(lista_filmes):
                    print(f'{i+1}. {produto}')
                    #len (lista_podutos) mostra a quantidade de produtos na lista.
                print(f'TOTAL DE PRODUTOS: {len(lista_produtos)}')
            input( '\n pressione uma tecla para continuar...')

        case 0:
            print('FIM')
            break
        case _:
            print('opçao invalida! ')
            input( '\n pressione uma tecla para continuar...')

