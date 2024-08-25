'''for c in range(1,10):
    print(c)
print('Fim')'''
n = 1
pares = 0
impares = 0
while n !=0:
    n= int(input('Digite um valor'))
    if n !=0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print('voce digitou {} números pares e {} números ímpares'.format(pares, impares))

