# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print ('-='* 20)
print ('Analizador de triângulos')
print ('-='* 20)
r1 = float(input('Primeiro segmento: '))
r2  = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('As três retas formam um triângulo')
else:
    print('As três retas não formam um triângulo')