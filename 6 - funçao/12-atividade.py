import os
os.system('cls')

def calcular_soma(nota1, nota2):
    soma = (nota1 + nota2)
    return soma

def calcular_divisao(nota1, nota2):
    if nota2 == 0:
        return 'Atençao! Divisao por zero'
    return nota1 / nota2


def calcular_multiplicacao(nota1, nota2):
    multiplicacao = (nota1 * nota2)
    return multiplicacao

def calcular_subtracao(nota1, nota2):
    return nota1 * nota2



print('= SOLICTANDO DADOS =')
nota1 = float(input('digite a primeiro nota: '))
nota2 = float(input('digite a segunda nota: '))

soma =calcular_soma(nota1, nota2)
divisao = calcular_divisao(nota1, nota2)
multiplicacao = calcular_multiplicacao(nota1, nota2)
subtracao = calcular_subtracao(nota1, nota2)

print('= SOLICTANDO DADOS =')
print(f'soma: {soma}')
print(f'divisao: {divisao}')
print(f'multiplicacao: {multiplicacao}')
print(f'subtracao: {subtracao}')