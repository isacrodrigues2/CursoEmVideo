salario = float(input('Digite seu salário R$'))
novo = salario + (salario * 15 / 100)
print('Seu salário atual é de R${:.2f} e após o reajuste de 15% passará a ser de R${:.2f}'.format(salario, novo))