import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class cliente:
    nome:str
    idade:int
    altura: float
lista_clientes = []

# SOLICITANDO DADOS DE UM CLIENTE
for i in range (2):
    dados_do_clientes = cliente(
        nome = input('digite seu nome: '),
        idade = int(input('digite sua idade: ')),
        altura = float(input('digite seu altura: '))
        )
    lista_clientes.append(dados_do_clientes)

for cliente in lista_clientes:
    print(f'nome:{cliente.nome}')
    print(f'idade:{cliente.idade}')
    print(f'altura:{cliente.altura}')
    print('='*15)
