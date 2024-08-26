d = int(input('Quantos dias alugados? '))
km = int(input('Quantos km percorridos? '))
calculo = ((d * 60) + (km * 0.15))
print('O Total a pagar é R${:.2f}'.format(calculo))