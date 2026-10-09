import os
os.system('cls')

contador = 0
soma = 0
qtd_notas = 2

while True:
    for i in range (qtd_notas):
        nota = float(input(f'digite sua nota: '))
    if nota <0 or nota > 10:
            print('\n nota invalida! ')
            input('pressione entrer para continuar')
            os.system('cls')
    else:
        soma += nota
        contador +=1
    if contador == 1:
                break

a = input('deseja inserir mais uma nota? S para sim ou N para nao. ')

if a == 'S':
    nota2 = float(input('infomre a tercira nota: '))
    soma += nota2
    media = soma / qtd_notas
    print(f'suam media é{media}')
else:
    media2 = soma /qtd_notas
    print(f'suan media é {media2}')