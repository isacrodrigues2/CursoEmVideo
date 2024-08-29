'''Exercício  Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
cont = 0
while True:
    num = int(input('quer ver a tabuada de qual valor? '))
    print('_'*30)
    if num < 0:
        break
    for cont in range (1,11):
        print(f'{num} x {cont} = {num * cont}')
    print('_'*30)
print('PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE')
input()