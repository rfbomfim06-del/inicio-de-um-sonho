import os
os.system('cls')

soma = 0
for i in range(4):
    nota = float(input('digite sua nota: '))
    soma = soma + nota

media = soma / 4

print(f'valor da sua nota:{nota}')
print(f'media:{media}')