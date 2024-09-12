'''brasil = []
estado1 = {'uf': 'Rio de de janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['Sigla'])'''

estado = dict()
brasil = list()
for c in range (0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
