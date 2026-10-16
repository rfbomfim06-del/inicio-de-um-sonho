import os
os.system('cls')

vetor_numeros = []
valor_negativo = 0
QUANTDADE = 5

for i in range(QUANTDADE):
    numero = int(input(f'digite o {i+1} numero: '))
    valor_negativo = (numero)
    if numero < 0:
        numero = 0
    vetor_numeros.append(numero)

print('\n = EXIBINDO DADOS =' )

for posicao, numero in enumerate(vetor_numeros, start=1):
    print(f'{posicao}º){numero}')