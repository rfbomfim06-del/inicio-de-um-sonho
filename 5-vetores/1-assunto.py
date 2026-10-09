import os
os.system('cls')

# print('= variaveis = ')
# variavel = 10
# variavel = 20
# print(f'valor da variavel: {variavel}')

# print('\n= vetores =')
# vetor = []
# vetor.append(10)
# vetor.append(20)
# vetor.append(30)
# print(f'valor do veotr na posiçao 1: {vetor[0]}')
# print(f'valor do veotr na posiçao 2: {vetor[1]}')
# print(f'valor do veotr na posiçao 3: {vetor[2]}')

vetor_nomes = []

for i in range(4):
    nomes = input(f'digite seu nome: ')
    vetor_nomes.append(nomes)

for i in range(4):
    print(f'nomes:{vetor_nomes[i]}')