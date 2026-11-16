import os
from datetime import date
os.system('cls')

def data_de_nascimento(data):
    ano_atual = date.today().year
    idade = ano_atual - data
    return idade

data = int(input('digite o ano do seu nascimento: '))
idade = data_de_nascimento(data)
print(f'Ano do nascimento:{data}')
print(f'anos:{idade}')
