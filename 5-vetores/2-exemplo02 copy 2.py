import os
os.system('cls')

print('= iserindo numero na vetor: =')
vetor_livros = []

for i in range(5):
    livros =input(f'digite o nome do {i+1}º livro: ')
    vetor_livros.append(livros)

print('\n= exibidno numeros do vetor: =')
for indice , livraria in enumerate(vetor_livros, start=1):
    print(f'{indice}º: {livraria}')
