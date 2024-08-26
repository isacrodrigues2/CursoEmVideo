'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR


– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date

atual = date.today().year
nasc = int(input('Informe o ano de nascimento do atleta: '))
ano = atual - nasc
print('O atleta tem {} anos'.format(ano))
if ano <= 9:
    print('Classificação: MIRIM')
elif ano <= 14:
    print('Classificação: INFANTIL')
elif ano <= 19:
    print('Classificação: JUNIOR')
elif ano <= 25:
    print('Classificação: SÊNIOR')
elif ano > 25:
    print('Classificação: MASTER')