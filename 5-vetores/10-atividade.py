import os
os.system('cls')

lista_produtos = []

while True:
    os.system('cls')
    print('''
=== MERDADO DENDEZEROS ===
1 - cadastra produto
2 - lista todos os protudos
3 - atualizar produto
4 - remover produto
5 - buscar por produto
0 - sair
''')

    opcao = int(input('Escolha uma opção: '))

    match opcao:

        case 1:
            #CREATE (INSERIR)
            print('== CADASTRAR PRODUTO ==')
            nome_produto = input('Digite o nome do novo produto: ').strip().upper()
            if nome_produto == '':
                print('o nome do produto deve ser inserido...')
            else:
                lista_produtos.append(nome_produto)
                print('Produto cadastrado com sucesso!')
        case 2:
            #READ(LER / BUSCAS)
            print('== PROTUDOS NO ESTOQUE ==')
            for produto in lista_produtos:
                print(f'- {produto}')
            print(f'Total:{len(lista_produtos)}')

        case 3:
            #UDATE(ATUALIZAR)
            print('=== ATUALIZAR PRODUTO ==')
            nome = input('qual produto deseja atualizar? ').strip().upper()
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input('novo nome: ').strip().upper()
                lista_produtos[posicao] = novo
                print('produto alterado com sucesso')
            else:
                print(' protudo nao encontrado.')

        case 4:
            #DELETE(REMOVER)
            print('=== REMOVER PRODUTO ==')
            nome = input('qual produto deseja remover? ').strip().upper()
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('produto excluido sucesso')
            else:
                print(' protudo nao encontrado.')

        case 5:
            #READ(LER / CONSULTA / BUSCAR)
            print('=== ENCONTRAR PRODUTO ==')
            nome = input('qual produto deseja remover? ').strip().upper()
            if nome in lista_produtos:
                print('produto emcontrado')
            else:
                print(' protudo nao esta no estoque.')
            

        case 0:
            print('Saindo do programa.....')
            break
        case _:
            print('\nOpção inválida! \nTente novamente....')

    input('Pressione uma tecla para continuar....').strip().upper()
    os.system('cls')