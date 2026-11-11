import os
os.system('cls')

def logo_senai():
    os.system('cls')
    print('\n')
    print('=' *15)
    print('     SENAI - BAHIA   ')
    print('=' *15)

logo_senai()
nome = input('digite seu nome: ')
email = input('digite seu email: ')
telefone = int(input('digite seu telefone: '))

print()
logo_senai()
print('=Exibindo dados = ')
print(f'nome:{nome}')
print(f'email:{email}')
print(f'telefone:{telefone}')