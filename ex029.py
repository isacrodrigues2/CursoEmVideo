print('*'*43)
print('**          Calculador de multa          **')
print('*'*43)
v = int(input('Insira a velocidade atual do carro: '))
if v > 80:
    print('Você foi multado!!')
    multa = (v - 80) * 7
    print('O valor da multa é de R${:.2f}'.format(multa))

print('Tenha um bom dia, dirija com segurança')
