import os
os.system('cls')

print('= insira a nota =')
vetor_nota = []

for i in range(3):
    nota = int(input('digite sua nota: '))
    vetor_nota.append(nota)

print('mostras notas')
for i in range(3):
    print(f'primeira posiçao do vetor:{vetor_nota[i]}')
# for indice , segretaria in enumerate(vetor_nota, start=1):
#     print(f'{indice}º: {segretaria}')

