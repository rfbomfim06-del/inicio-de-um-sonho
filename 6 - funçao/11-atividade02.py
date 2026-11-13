import os
os.system('cls')

def verificar_numero( numero):
    if  numero > 0:
        resultado = 'POSITIVO'
    elif numero == 0:
        resultado = 'NEUTRO'
    else:
        resultado = 'NEGATIVO'
    return(resultado)


print('= SOLICTANDO DADOS =')
numero = int(input('digite o   numero: '))

resultado = verificar_numero( numero)

print('= SOLICTANDO DADOS =')
print(f'o  numero { numero} é {resultado}')
