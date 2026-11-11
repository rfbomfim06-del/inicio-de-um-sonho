import os
os.system('cls')

def mostrar_saudacao(nome, idade):
    print(f'{nome} tem {idade} anos.')

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')


print('=Exibindo dados = ')
mostrar_saudacao(nome, idade)