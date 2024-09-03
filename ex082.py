'''Exercício  Python 082: Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente.
 Ao final, mostre o conteúdo das três listas geradas.'''
valores = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
input()