import os
os.system('cls')


#funçao
def cabecalho():
    print('\n')
    print('=' *15)
    print('            senai')
    print('=' *15)


#usando funçao.
cabecalho()
nome = input('digite seu nome: ')

cabecalho()
idade = input('digite sua idade: ')

cabecalho()
print(f'nome: {nome}')
print(f'idade: {idade}')