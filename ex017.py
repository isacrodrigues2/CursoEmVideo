from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))



'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (co**2 + ca**2)**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))'''