from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome:str
    telefone:str
    email:str


#fençao dentro da classe
    def mostrar_dados(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print(f'email: {self.email}')
        print('='*15)
#fuçao somente para enviar e-mail
    def email_marketing(self):
        print(f'nome: {self.nome}')
        print(f'email: {self.email}')
        print('='*15)

    def whatsapp_marketing(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print('='*15)

lista_clientes = []


for i in range (1):
    dados_do_clientes = Cliente(
        nome = input('digite seu nome:'),
        telefone = input('digite seu telefone: '),
        email = input('digite seu email: ')
    )
    lista_clientes.append(dados_do_clientes)

print('\n== EXIBINDO DADOS ==')
for cliente in lista_clientes:
    cliente.mostrar_dados()

print('\n== EXIBINDO EMAIL ==')
for cliente in lista_clientes:
    cliente.email_marketing()

print('\n== EXIBINDO WHATSAPP ==')
for cliente in lista_clientes:
    cliente.whatsapp_marketing()