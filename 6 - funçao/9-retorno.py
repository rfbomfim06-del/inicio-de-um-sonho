import os
os.system('cls')

def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2)
    return resultado


print('= SOLICTANDO DADOS =')
nota1 = float(input('digite a primeiro nota: '))
nota2 = float(input('digite a segunda nota: '))

soma =calcular_notas(nota1, nota2)

print('= SOLICTANDO DADOS =')
print(f'soma: {soma}')