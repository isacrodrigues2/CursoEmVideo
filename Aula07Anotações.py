n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
soma= n1+n2
subtracao= n1-n2
multiplicacao= n1*n2
divisao= n1/n2
elevacao= n1**n2
divisao_inteira= n1//n2
resto= n1%n2
print( ' {} mais {} é igual a {}!'.format(n1, n2, soma))
print( '{} menos {} é igual a {}!'.format(n1, n2, subtracao))
print( '{} vezes {} é igual a {}!'.format(n1, n2, multiplicacao))
print( '{} divido por {} é igual a {}!'.format(n1, n2, divisao))
print( '{} elevado a {} é igual a {}!'.format(n1, n2, elevacao))
print( 'A divisão inteira de {} por {} é igual a {}!'.format(n1, n2,divisao_inteira))
print('O resto da divisão inteira entre {} e {} é {}!'.format(n1, n2, resto))