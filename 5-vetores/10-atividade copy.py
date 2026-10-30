import os
os.system('cls')

lista_paciente = []

while True:
    os.system('cls')
    print('''
=== CADASTRO DE PACIENTES ===
1 - cadastra paciente
2 - lista todos os protudos
3 - atualizar paciente
4 - remover paciente
5 - buscar por paciente
0 - sair
''')

    opcao = int(input('Escolha uma opção: '))

    match opcao:

        case 1:
            #CREATE (INSERIR)
            print('== CADASTRAR DO CLIENTE ==')
            nome_paciente = input('Digite o seu nome e sobrenome : ').strip().upper()
            if nome_paciente == '':
                print('o nome do paciente deve ser inserido...')
            else:
                lista_paciente.append(nome_paciente)
                print('Paciente cadastrado com sucesso!')
        case 2:
            #READ(LER / BUSCAS)
            print('== LISTA DOS PACIENTES ==')
            for posicao, nome_paciente in enumerate(lista_paciente, start=1):
                print(f'{posicao}º) {nome_paciente}')
            print(f'Total:{len(lista_paciente)}')

        case 3:
            #UDATE(ATUALIZAR)
            print('=== ATUALIZAR LISTA ==')
            nome = input('qual paciente deseja atualizar? ').strip().upper()
            if nome in lista_paciente:
                posicao = lista_paciente.index(nome)
                novo = input('novo nome: ').strip().upper()
                lista_paciente[posicao] = novo
                print('paciente alterado com sucesso')
            else:
                print(' protudo nao encontrado.')

        case 4:
            #DELETE(REMOVER)
            print('=== REMOVER PACIENTE ==')
            nome = input('qual paciente deseja remover? ').strip().upper()
            if nome in lista_paciente:
                lista_paciente.remove(nome)
                print('paciente excluido sucesso')
            else:
                print(' protudo nao encontrado.')

        case 5:
            #READ(LER / CONSULTA / BUSCAR)
            print('=== ENCONTRAR PACINTE ==')
            nome = input('qual paciente deseja encontrar? ').strip().upper()
            if nome in lista_paciente:
                print('paciente encontrado')
            else:
                print(' paciente nao esta no sistema.')
            

        case 0:
            print('Saindo do programa.....')
            break
        case _:
            print('\nOpção inválida! \nTente novamente....')

    input('Pressione uma tecla para continuar....').strip().upper()
    os.system('cls')