# galera = [['Isac', 26],['josias', 27], ['Regina', 53], ['Sebastião', 69]]
# print(galera[0][0])
# for p in galera:
 #   print(f'{p[0]}')

# colocando dados manualmente dentro da lista
galera = list()
dados = list()
totmai = totmen = 0
for c in range (0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')