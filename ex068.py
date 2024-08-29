'''Exercício  Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
v = 0
from random import randint
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar: [P/I] ')).strip().upper()[0]
    print(f'O computador escolheu {computador} e você escolheu {jogador}. o total foi de {total}')
    print('DEU PAR' if total % 2==0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Não gostei, vamos jogar novamente...')
print(f'GAME OVER voce ganhou {v} vezes')
input()