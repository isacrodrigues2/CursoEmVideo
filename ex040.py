'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, d acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média= (n1 + n2) / 2
print('Com {:.1f} e {:.1f} a sua média é {:.1f}'.format(n1, n2, média))
if 10 > média >= 9:
    print('Aluno APROVADO')
    print('Parabéns!!')
elif média == 10:
    print('Aluno APROVADO')
    print('Muito bem seu C.D.F!!')
elif 7 <= média < 9:
    print('Aluno APROVADO')
elif  7 > média >= 5:
    print('Passou raspando')
    print('Aluno em RECUPERAÇÂO')
elif média < 5:
    print('Aluno REPROVADO')
    print('Escorregou no quiabo')