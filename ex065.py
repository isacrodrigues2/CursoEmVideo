'''Exercício  Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


resposta = 'S'
soma = cont = média = maior = menor = 0
while resposta != 'N':
    num = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    cont +=1
    soma += num
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num< menor:
        menor = num
média = soma / cont
print('você digitou {} números a média entre eles foi {}'.format(cont, média))
print('O maior numero entre eles foi {} e o menor foi {}'.format(maior, menor))
input()
