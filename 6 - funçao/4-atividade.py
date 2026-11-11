import os
os.system('cls')

while True:
    def logo_senai():
        os.system('cls')
        print('\n')
        print('=' *15)
        print('     CLIMEDI   ')
        print('=' *15)
        print('= CADASTRO =')

    print('''
    1- cadastrar cliente
    2 - mostrar dados do cliente
    3- sair
    ''')
    opcao = int(input('digite a opção: '))
    match opcao:
        case 1:
            logo_senai()
            nome = input('digite seu nome: ')
            email = input('digite seu email: ')
            telefone = int(input('digite seu telefone: '))
        case 2:
            print()
            logo_senai()
            print('=Exibindo dados = ')
            print(f'nome:{nome}')
            print(f'email:{email}')
            print(f'telefone:{telefone}')
        case _:
            print('SAINDO')
            os.system('cls')
            break
