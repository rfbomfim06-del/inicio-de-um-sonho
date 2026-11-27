from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Clientes:
    nome:str
    idade:str
    altura:float

lista_clientes = []

#salvando em um arquivo.
arquivo = 'dados_clientes.csv'
with open(arquivo, 'r') as arquivo_clientes:
    for linha in arquivo_clientes:
        nome,idade,altura = linha.strip().split(',')
        lista_clientes.append(Clientes(
        nome = nome,
        idade = int(idade),
        altura = float(altura)
        ))

for cliente in lista_clientes:
    print(f'nome:{cliente.nome}')
    print(f'idade:{cliente.idade}')
    print(f'altura:{cliente.altura}')
    print('='*15)