import os
os.system('cls')

print('= insira a nota =')
vetor_numero = []
QUANTIDADE_DE_NOTAS= 5
# maior_numero = 0
# menor_numero = 999
par = 0
impar = 0

for i in range(QUANTIDADE_DE_NOTAS):
    numero = int(input('digite um numero: '))
    vetor_numero.append(numero)
    if numero % 2 == 0:
        par +=1
    else:
        impar +=1

# maior_numero = max(vetor_numero)
# menor_numero = min(vetor_numero)

print('mostrar numero')
for posicao , numero in enumerate(vetor_numero, start=1):
    print(f'{posicao}º: {numero}')

# print(f'maior_numero: {maior_numero}')
# print(f'menor_numero: {menor_numero}')