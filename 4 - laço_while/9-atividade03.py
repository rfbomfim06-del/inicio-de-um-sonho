import os
os.system('cls')

soma = 0
quantidade = 0

with True:
    numero = int(input('digite um numero: '))
    if numero <0:
    soma += numero
    quantidade +=1

if quantidade > 0:
    media = soma /quantidade
    print(f' amedia aritimetica doas {quantidade} numeros digitados é: {media}')
else:
    print('nehum numero posito')