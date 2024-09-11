

filme = {
    'titulo': 'Star wars',
    'ano' : '1977',
    'diretor': 'george lucas'
}
# pegar só os valores
print(filme.values())
# pegar só os keys
print(filme.keys())
#pegar tanto os valores quantos os keys
print(filme.items())
# para cada 'k' ou key havéra valores "v" dentro de items
for k,v in filme.items():
    print(f'O {k} é {v}')