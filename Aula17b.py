valores = list()
#ler vários valores pelos teclado colocando dentro de uma lista
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
#for v in valores:
   # print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')