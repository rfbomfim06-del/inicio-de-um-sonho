import os
os.system('cls')

# soma = 0
# quantidade_nota = 2
# for i in range (quantidade_nota):
#     while True:
#         nota = float(input('digite a {i+1}ª nota entre 0 e  10: '))
#         if nota >= 0 and nota <= 10:
#             soma = soma = soma + nota
#             break
        
#         else:
#             print()
#             print('nota invalida')

# media = soma / quantidade_nota
# print(f'media: {media}')
# print('== FIM ==')





soma = 0
quantidade_nota = 2
for i in range (quantidade_nota):
    while True:
        nota = float(input('digite a {i+1}ª nota entre 0 e  10: '))
        if nota <= 0 or nota >= 10:
            print()
            print('nota invalida')
            break
        
        else:
            print()
            soma = soma = soma + nota

media = soma / quantidade_nota
print(f'media: {media}')
print('== FIM ==')
