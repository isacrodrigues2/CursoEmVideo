'''Exercício  Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:


A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

totidade = tothomens = totmulhermenos20 = 0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('='*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F]')).strip().upper()[0]
        if idade >= 18:
            totidade += 1
        if sexo == 'M':
            tothomens += 1
        if sexo == 'F' and idade < 20:
            totmulhermenos20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {totidade}')
print(f'Total de homens digitados {tothomens}')
print(f'Total de mulhers com menos de 20 anos {totmulhermenos20}')
input()