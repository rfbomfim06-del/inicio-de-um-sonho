import os
os.system('cls')

# numero_1 = int(input('digite um numero: '))
# numero_2 = int(input('digite um numero: '))
# numero_3 = int(input('digite um numero: '))
# numero_4 = int(input('digite um numero: '))
# numero_5 = int(input('digite um numero: '))

# soma = numero_1 + numero_2 + numero_3 + numero_4 + numero_5
# print(f'soma:{soma}')

soma = 0
for i in range(3):
    numero = int(input('digite um numero: '))
    soma = numero + soma

print(f'soma:{soma}')