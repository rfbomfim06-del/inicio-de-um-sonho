import os
os.system('cls')

print('= insira a nota =')
vetor_nota = []
QUANTIDADE_DE_NOTAS= 3
for i in range(QUANTIDADE_DE_NOTAS):
    nota = int(input('digite sua nota: '))
    vetor_nota.append(nota)

soma = sum(vetor_nota)
media = soma / QUANTIDADE_DE_NOTAS
# media = sum(vetor_nota) / quantidade_de_notas
print('mostras notas')
for posicao , nota in enumerate(vetor_nota, start=1):
    print(f'{posicao}º: {nota}')

print(f'soma: {soma}')
print(f'media: {media}')
