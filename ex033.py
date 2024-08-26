# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro número: '))
b = int(input('segundo número: '))
c = int(input('terceiro número: '))

# Verificando quem é menor
menor = a
if b < a and b < c:
    menor= b
if c < a and c < b:
    menor= c

# Verificando quem é maior
maior = a
if b > a and b > c:
    maior= b
if c > a and c > b:
    maior= c

print('O maior número dos três é {}, e o menor é {}'.format(maior, menor))