import os
os.system('cls')

vetor_pratos = []
vetor_precos = []

while True:
    print('''
codigo              prato                preco
1                   picanha              R$25,00
2                   lasanha              R$20,00
3                   strogonoff           R$ 18,00
4                   bife acebolado       R$15,00
5                    pao com ovo          R$5,00
''')
    opcao = int(input('digite a opçao desejada: '))

    match opcao:
        case '1':
            prato = 'picanha'
            preco = 25
        case '2':
            prato = 'lasanha'
            preco = 20
        case '3':
            prato ='stogonoff'
            preco = 18
        case '4':
            prato = 'bife acebolado'
            preco = 15
        case '5':
            prato = 'pao com ovo'
            preco = 5
        case _:
            print('opcao invalida')

    if opcao >= 1 and opcao <= 5:
        vetor_pratos.append(prato)
        vetor_precos.append(prato)

    continuar = input('deseja escolher outro prato?\n responda S ou N').upper()
    if continuar == 'N':
        break
    os.system('cls')

if sum(vetor_precos) == 0:
    print('\nnenhumprato selecionado.')
else:
    print('\n= PRATOS ESCOLHIDOS =')
    for i, prato in enumerate(vetor_pratos, start=1):
        print(f'{i}º prato: {prato}')
    print(f'\nTotal: R$ {sum(vetor_precos)}')

print('\nVolte sempre!')

