import os
os.system('cls')

vetor_numeros = []
soma_positivos = 0
qauntidade_impares = 0
QUANTDADE = 5

for i in range (QUANTDADE):
    numero = int(input('digite o numero: '))
    vetor_numeros.append(numero)
    if numero > 0:
        soma_positivos += numero
    else:
        qauntidade_impares += 1

print(f'soma dos numeros positivos: {soma_positivos}')
print(f'soma dos numeros impares: {qauntidade_impares}')