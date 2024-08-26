# Feitas as correções de calendário, definiu-se a nova regra para o cálculo dos anos bissextos:
# De 4 em 4 anos é ano bissexto.
# De 100 em 100 anos não é ano bissexto.
# De 400 em 400 anos é ano bissexto.
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BiSSEXTO'.format(ano))
else:
    print('O ano {} NÂO é BiSSEXTO'.format(ano))