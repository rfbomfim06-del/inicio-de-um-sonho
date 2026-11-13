import os
os.system('cls')

def logo_senai():
    os.system('cls')
    print('=' *15)
    print('       SENAI')
    print('=' *15)

def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos')


logo_senai()
print('\n= SOLICITANDO DADOS =')
nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))

logo_senai()
print('\n= EXIBINDO DADOS =')

mostrar_dados(nome, idade)