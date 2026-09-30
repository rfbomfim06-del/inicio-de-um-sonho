import os
os.system('cls')

while True:
    nota = int(input('digite sua nota: '))
    if nota < 0  or nota > 10:
        print()
        print('Nota invalida')
    else:
        print()
        print(f'sua nota é: {nota}')
        break

print('== FIM ==')