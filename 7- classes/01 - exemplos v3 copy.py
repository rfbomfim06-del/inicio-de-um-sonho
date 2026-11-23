import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class cliente:
    nome:str
    idade:int

lista_clientes = []

# SOLICITANDO DADOS DE UM CLIENTE
lista_clientes.append(cliente("marta",30))
lista_clientes.append(cliente("jose",40))

for cliente in lista_clientes:
    print(f'nome:{cliente.nome}')
    print(f'idade:{cliente.idade}')
    print('='*15)
