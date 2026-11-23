from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome:str
    idade:str
    telefone:str
    endereco:str


    def mostrar_dados(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print(f'endereco: {self.endereco}')
        print(f'idade: {self.idade}')
        print('='*15)

    def dados_pessoais(self):
        print(f'nome:{self.nome}')
        print(f'idade:{self.idade}')

    def localizacao_cliente(self):
        print(f'nome:{self.nome}')
        print(f'telefone:{self.telefone}')

lista_clientes = []

for i in range (1):
    dados_do_clientes = Cliente(
        nome = input('digite seu nome:'),
        telefone = input('digite seu telefone: '),
        endereco = input('digite seu endereço: '),
        idade = input('digite sua idade: ')
    )
    lista_clientes.append(dados_do_clientes)

print('\n== EXIBINDO DADOS ==')
for cliente in lista_clientes:
    cliente.mostrar_dados()

print('\n== EXIBINDO PESSOAL ==')
for cliente in lista_clientes:
    cliente.dados_pessoais()

print('\n== EXIBINDO ENDEREÇO ==')
for cliente in lista_clientes:
    cliente.localizacao_cliente()