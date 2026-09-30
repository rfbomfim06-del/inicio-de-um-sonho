import os
os.system('cls')

while True:
    numero = int(input('digite um numero entre 1 e 10: '))
    if numero < 1 or numero >10:
        print()
        print('numero invalido,tente novamente!')
    else:
        print()
        print('o numero esta entre 1 e 10.')
        break # serve para parar o laço de repetiçao.

print('== FIM ==')

