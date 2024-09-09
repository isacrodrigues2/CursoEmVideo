from random import randint
from time import sleep

lista = list()
jogos = []
print('=' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 1
cont = 0
while tot <= quant:
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    cont = 0
    tot +=1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print ('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3 )
for i, v in enumerate(jogos):
    print(f'Jogo {i+1} {v}')
    sleep(1)

print('-=' * 5, '< BOA SORTE! >', '-='*5)
input()