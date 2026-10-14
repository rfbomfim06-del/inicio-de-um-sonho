import os
os.system('cls')

print('= iserindo numero na vetor: =')
vetor_numeros = []

for i in range(3):
    numero = int(input('digite o valor do vetor: '))
    vetor_numeros.append(numero)

print('\n= exibidno numeros do vetor: =')
for i in range(3):
    print(f'primeira posiçao do vetor::{vetor_numeros[i]}')
