import os
os.system('cls')

login = 'robi'
senha = 123
while True:
    login = (input('digite seu login: '))
    senha = int(input('digite a sua senha: '))
    if login == 'robi' and senha == 123:
        print()
        print('login e senha correto')
        break
    else:
        print()
        print('senha ou login errado!. tente novamente')
        input('pressione uma tecla para continuar...')
        os.system('cls')






login = 'robi'
senha = 123
while True:
    login = (input('digite seu login: '))
    senha = int(input('digite a sua senha: '))
    if login != 'robi' or senha != 123:
        print()
        print('senha ou login errado!. tente novamente')
        break
    else:
        print()
        print('login e senha correto')
        os.system('cls')
#! negaçao