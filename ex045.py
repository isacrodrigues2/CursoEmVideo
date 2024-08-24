'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
itens =  ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2) 
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual e a sua jogada? '))
print('JO')
sleep(1)
print('kEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-='*15)
if computador == 0: # Compuatdor jogou pedra
    if jogador == 0: 
        print('EMPATE')
    elif jogador == 1:
        print('jogador GANHOU!!')
    elif jogador == 2:
        print('computador GANHOU!!')
    else:
        print('Jogada inválida')
elif computador == 1: # Compuatdor jogou papel
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('jogador GANHOU!!')
    elif jogador == 0:
        print('computador GANHOU!!')
    else:
        print('Jogada inválida')
elif computador == 2: # Compuatdor jogou pedra
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('jogador GANHOU!!')
    elif jogador == 1:
        print('computador GANHOU!!')
    else:
        print('Jogada inválida')