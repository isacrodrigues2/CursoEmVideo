'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual o valor do salário do funcionário? '))
if salario > 1250:
    salario_novo =  salario + (salario * 10 / 100)
else:
    salario_novo = salario + (salario * 15 / 100)

print('Quem recebia R${:.2f} vai passar a receber R${:.2f}'.format(salario, salario_novo))