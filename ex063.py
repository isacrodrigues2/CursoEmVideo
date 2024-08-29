'''Exercício  Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''


print('-='* 11)
print('GERADOR DE FIBONACCI')
print('-='* 11)

n = int(input('Quantos termos você quer calcular? '))
t1 = 0
t2 = 1
cont = 3
print('{} → {}'.format(t1 , t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' → FIM')
input()