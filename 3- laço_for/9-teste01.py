import os
os.system('cls')

# print('ACUMOLANDO CALORES EM UMA VARIEVEL')
# soma = 0

# print(f'VALOR INICIAL da variavel soma:{soma}')

# for i in range(3):
#     numero = int(input('digite um numero: '))
#     soma = numero + soma
#     print(f'valor temporario da variavel soma:{soma}')

# # print(f'soma:{soma}')
# print(f'valor final da variavel soma:{soma}')

soma = 10
for i in range(3):
    soma += int(input('digite um numero: '))
print(f'valor final da variavel soma:{soma}')
