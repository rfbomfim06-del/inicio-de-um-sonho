from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class clientes:
    nome:str
    email:str
    telefone:str
    endereco:str

QUANTIDADE_CLIENTEs = 3

lista_clientes = []

arquivo = 'dados_clientes.csv'
with open(arquivo,'r') as arquivo_clientes:
    for linha in arquivo_clientes:
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
