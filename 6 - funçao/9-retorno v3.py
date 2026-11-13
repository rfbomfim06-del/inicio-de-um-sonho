import os
os.system('cls')

def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) /2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = ('APROVADO')
    else:
        resultado = ('REPROVADO')
    return resultado
print('= SOLICTANDO DADOS =')
nota1 = float(input('digite a primeiro nota: '))
nota2 = float(input('digite a segunda nota: '))

media = calcular_notas(nota1, nota2)
situacao = verificar_resultado(media)
print('= SOLICTANDO DADOS =')
print(f'media: {media}')
print(f'resultado: {situacao}')
