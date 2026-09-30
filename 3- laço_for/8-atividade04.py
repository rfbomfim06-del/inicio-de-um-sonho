import os
os.system('cls')

qauntidade_repeticoes = 5
pares = 0
impares = 0

for i in range(3):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f'quatidade de pares:{pares}')
print(f'quatidade de impares:{impares}')
