'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor = float(input('Valor da casa: R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento: '))
parcela = valor /(anos * 12)
print('Para pegar um empréstimo de RS{:.2F} para pagar em {} anos, o valor da parcela será de R${:.2f}'.format(valor, anos, parcela))
if parcela > (salario * 30 / 100):
    print('Empréstimo NEGADO')
else:
    print('Empréstimo pode ser CONCEDIDO')