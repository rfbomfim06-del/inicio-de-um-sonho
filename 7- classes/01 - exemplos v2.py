import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class cliente:
    nome:str
    idade:int
# SOLICITANDO DADOS DE UM CLIENTE
cliente1 = cliente('marta',30)


# SOLICITANDO DADOS DE OUTRO CLIENTE
cliente2 = cliente('jose',40)

print(f'nome:{cliente2.nome}')
print(f'idade:{cliente2.idade}')

print(f'nome:{cliente1.nome}')
print(f'idade:{cliente1.idade}')