aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno ["Nome"]}: '))
print('-=' *30)
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif  5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k , v in aluno.items():
    print(f' {k} é {v}')