import os
os.system('cls')

print('= insira a nota =')
vetor_nota = []
def notas(vetor_nota):
    nota = vetor_nota
    return nota

QUANTIDADE_DE_NOTAS= 3
for i in range(QUANTIDADE_DE_NOTAS):
    nota = int(input('digite sua nota: '))
    vetor_nota.append(nota)


soma = sum(vetor_nota)
media = soma / QUANTIDADE_DE_NOTAS
print('mostras notas')
for posicao , nota in enumerate(vetor_nota, start=1):
    print(f'{posicao}º: {nota}')

print(f'media: {media}')
