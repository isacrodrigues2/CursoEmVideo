'''Exercício  Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

numeros = (int(input('Primeiro valor: ')),
           int(input('Segundo valor: ')),
           int(input('Terceiro valor: ')),
           int(input('Quarto valor: ')))
cont = 0
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado')
print('O valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f' {n} ', end='')

input()