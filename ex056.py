'''Exercício  Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('_____ {}° PESSOA _____'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ' )).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem= idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / p
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(totmulher20))