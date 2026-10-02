import os
os.system('cls')


codigo = int(input('digite o codigo: '))
print()
print('== MERCADO ==')
print(' Suco R$ 2,0')
print(' Cafe R$ 2,50')
print(' pao R$ 3,00')
print(' biscoito R$ 5,00')
print(' carne R$ 10,00')
print()
while True:
    match codigo:
        case 1:
            print('Suco')
            print('R$ 2,0')
            break
        case 2:
            print('Cafe')
            print('R$ 2,50')
            break
        case 3:
            print('Pao')
            print('R$ 3,00')
            break
        case 4:
            print('Biscoito')
            print('R$ 5,00')
            break
        case 5:
            print('Carne')
            print('R$ 10,00')
            break
        case _:
            print('numero invalido')
            break
