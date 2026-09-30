import os
os.system('cls')
soma = 0
for i in range(3):
    nota = float(input('digite sua nota: '))
    soma = soma + nota

media = soma / 3
if media >= 7:
    print('VOCE ESTA APROVADO')
elif media >=4:
    print('VOCE ESTA EM RECUPERAÇAO')
else:
    print('VOCE ESTA REPROVADO')
print(f'valor da sua nota:{nota}')
print(f'media:{media}')