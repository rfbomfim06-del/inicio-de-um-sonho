import os
os.system('cls')

def tabuada():
    for i in range (1,11):
        print(f'{numero} x {i} = {numero * i} ')


print('= SOLICITANDO DADOS =')
numero = int(input('digite um numero: '))

print('\n =EXIBINDO DADOS=')
mostrar_tabuada(numero)