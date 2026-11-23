from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome:str
    telefone:str
    email:str

lista_clientes = []

for i in range (1):
    dados_do_clientes = Cliente(
        nome = input('digite seu nome:'),
        telefone = input('digite seu telefone: '),
        email = input('digite seu email: ')
    )
    lista_clientes.append(dados_do_clientes)

for cliente in lista_clientes:
    print(f'nome: {cliente.nome}')
    print(f'telefone: {cliente.telefone}')
    print(f'email: {cliente.email}')
    print('='*15)