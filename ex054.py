from datetime import date
atual = date.today().year
menor= 0
maior = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior+= 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))
print('E também tivemos {} pessoas maiores de idade'.format(maior))
