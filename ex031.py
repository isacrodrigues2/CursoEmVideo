

distancia = int(input('Qual a distancia da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}km'.format(distancia))
preco = 0.45 if distancia > 200 else 0.50
print('O valor da sua passagem será de R${:.2f}'.format( (distancia * preco)))