from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class clientes:
    nome:str
    email:str
    telefone:str
    endereco:str

QUANTIDADE_CLIENTEs = 1

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
    arquivo = 'dados_fornecedor.csv'
    with open(arquivo, 'w') as arquivo_fornecedor:
        for cliente in lista_clientes:
            arquivo_fornecedor.write(f'{cliente.nome}, {cliente.email}, {cliente.telefone}, {cliente.endereco}\n')

    print('cliente salvo com sucesso')