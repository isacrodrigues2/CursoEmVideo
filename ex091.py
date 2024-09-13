'''Exercício  Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
ranking = list
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} jogou {v}')
    sleep(1)
print('_='* 30)
print(' == RANKING == ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'O {i+1}° foi {v[0]} que jogou {v[1]}')
    sleep(1)