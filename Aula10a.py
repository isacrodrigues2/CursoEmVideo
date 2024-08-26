
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
média = (n1 + n2) / 2
if média >= 6:
    print('A sua média é {:.1f} você passou!'.format(média))
else:
    print('A sua média é {:.1f} você escorregou no quiabo'.format(média))