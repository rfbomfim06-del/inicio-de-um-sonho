import os
os.system('cls')

print('= insira a nota =')
vetor_nota = []
QUANTIDADE_DE_NOTAS= 4

for i in range(QUANTIDADE_DE_NOTAS):
    nota = int(input('digite sua nota: '))
    vetor_nota.append(nota)
    soma = sum(vetor_nota)
    media = soma / QUANTIDADE_DE_NOTAS



if nota >=7:
    print('aprovado')
elif nota >= 5:
    print('recuperaçao')
else:
    print('reprovado')


print(f'soma: {soma}')
print(f'media: {media}')