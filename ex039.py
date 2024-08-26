'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


from datetime import date

nasc = int(input ('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Ta na hora de se alistar')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    if saldo == 1:
        print('Ainda falta {} ano para se alistar'.format(saldo))
    else:
        print('Ainda faltam {} anos para se alistar'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    if saldo == 1:
        print('você deveria ter se alistado a {} ano atrás'.format(saldo))
    else:
        print('você deveria ter se alistado a {} anos atrás'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))