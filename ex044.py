'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJINHA DA ESQUINA '))
preço = float(input('Informe o valor da compra: R$'))
total = 0
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcelas = 2
    print('Sua compra será parcelada em 2 vezes SEM Juros \ne o valor da sua parcela será de {:.2f}'.format(total/parcelas))
elif opção == 4:
    total = preço
    parcelas = int(input('informe a quantidade de parcelas: '))
    total = preço + (preço * 20 / 100)
    print('Sua compra será parcelada em {} vezes, \ne o valor da sua parcela será de {:.2f}'.format(parcelas, total/parcelas))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento, tente novamente!!')
print('Sua compra de {:.2f} vai dar {:.2f}'.format(preço, total))
