'''Exercício  Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.


b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

clubes = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense',
          'Palmeiras', 'Grêmio','Corinthians', 'Bragantino', 'Santos',
          'Athletico-PR', 'Atlético-GO', 'Ceará SC', 'Sport Recife',
         'Fortaleza', 'Bahia', 'Vasco da Gama', 'Coritiba', 'Botafogo')
print('='*30)
print(f'lista de times: {clubes}')
print('='*30)
print(f'OS cinco primeiros colocados são: {clubes[0:5]}')
print('='*30)
print(f'Os quatro últimos são: {clubes[-4:]}')
print('='*30)
print(f'os times em ordem alfabética são: {sorted(clubes)}' )
print('='*30)
print(f'O flamengo está na {clubes.index('Flamengo')+1}° posição')