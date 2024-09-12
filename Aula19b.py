pessoas = { 'nome': 'Isac',
            'sexo' : 'M',
            'idade': 26 }
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# mostrar valores das keys do dicionário
print(pessoas.keys())
# mostrar valores do dicionário
print(pessoas.values())
# acessando os valores das keys por laços
for k in pessoas.keys():
    print(k)
# acessando os valores dos itens por laços
for k, v in pessoas.items():
    print(f'{k} = {v}')