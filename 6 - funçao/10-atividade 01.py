import os
os.system('cls')



def verificar_par_impar(numero):
    if numero % 2 == 0:
        resultado = 'pares'
    else:
        resultado = 'impares'
    return resultado


print('= SOLICTANDO DADOS =')
numero1 = int(input('digite o  numero: '))

resultado = verificar_par_impar(numero1)

print('= SOLICTANDO DADOS =')
print(f'o numero {numero1} é {resultado}')
