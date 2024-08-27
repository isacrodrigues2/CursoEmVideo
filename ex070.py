'''Exercício  Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.


B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total = maiorque1000 = menor = cont = 0
barato = ' '
print('='* 30)
print('{:-^30}'.format(' LOJA SUPER BARATÃO '))
print('='* 30)
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço R$'))
    cont += 1
    total += valor
    if cont == 1 or menor > valor:
        menor = valor
        barato = produto
    if valor > 1000:
        maiorque1000 +=1
    resp = ' '
    while resp not in 'SN':
        resp= str(input('Quer continuar sua compra? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' OBRIGADO, VOLTE SEMPRE '))
print(f'O total da compra foi de R${total:.2f}')
print(f'{maiorque1000} produtos custaram mais de R$1.000,00')
print(f'o produto mais barato foi {barato} que custou R${menor:.2f}')