import os
os.system('cls')

# logins = 'robi'
# senhas = '123'

# quantidade_de_tentativas = 3
# for i in range (quantidade_de_tentativas):
#     login = input('digite seu login: ')
#     senha = input('digite a sua senha: ')
#     if login == logins and senha == senhas:
#         print()
#         print('login e senha correto')
#     else:
#         print()
#         print('Voce foi bloqueado!. tente mais tarde')
#         input('pressione uma tecla para continuar...')
#         os.system('cls')



logins = 'robi'
senhas = '123'
quantidade_de_tentativas = 3

for i in range(quantidade_de_tentativas):
    login = input('digite seu login: ')
    senha = input('digite sua senha: ')
    if login == logins and senha == senhas:
        print ('bem-vindo')
    else:
        print('Voce foi bloqueado!. tente mais tarde')
        input('pressione uma tecla para continuar...')
        os.system('cls')