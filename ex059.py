'''Exercício  Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('QUal é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            print('entre {} e {} O maior número é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('entre {} e {} O maior número é {}'.format(n1, n2, n2))
        else:
            print('Os números são iguais')
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input("Informe o primeiro número: "))
        n2 = int(input("Informe o segundo número: "))
    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida! tente novamente')
    print('_=' * 10)
sleep(2)
print('Fim do programa, volte sempre!')
