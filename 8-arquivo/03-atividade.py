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

for i in range(QUANTIDADE_CLIENTEs):
    novo_cliente = clientes(
        nome= input('digite seu nome: '),
        email= input('digite seu email: '),
        telefone= float(input('digite seu telefone: ')),
        endereco= input('digite seu endereço: ')
    )
    lista_clientes.append(novo_cliente)

    #salvando em um arquivo.
    arquivo = 'dados_clientes.csv'
    with open(arquivo, 'a') as arquivo_clientes:
        for cliente in lista_clientes:
            arquivo_clientes.write(f'{cliente.nome}, {cliente.email}, {cliente.telefone}, {cliente.endereco}\n')

    print('cliente salvo com sucesso')