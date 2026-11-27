from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class clientes:
    nome:str
    email:str
    telefone:str
    endereco:str



lista_clientes = []

arquivo = 'dados_fornecedor.csv'
with open(arquivo,'r') as arquivo_fornecedor:
    for linha in arquivo_fornecedor:
        nome,email,telefone,endereco = linha.strip().split(',')
        lista_clientes.append(clientes(
            nome = nome,
            email= email,
            telefone= telefone,
            endereco= endereco
        ))

for cliente in lista_clientes:

    print(f'nome:{cliente.nome}')
    print(f'email:{cliente.email}')
    print(f'telefone:{cliente.telefone}')
    print(f'endereco:{cliente.endereco}')
    print('='*85)