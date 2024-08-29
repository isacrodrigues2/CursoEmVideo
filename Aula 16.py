lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# tuplas são imutáveis
#print(lanche[-4:])
# tuplas são imutáveis
#for comida in lanche:
 #   print(f'Eu vou comer {comida}')
#for cont in range (0, len(lanche)):
 #print(f'Eu vou comer {lanche[cont]} na posicão {cont}')

#for pos,  comida in enumerate(lanche):
#print(f'Eu vou comer {comida} na posição {pos}')
#print(sorted(lanche)) # colocar em ordem

#print('Comi pra caramba!')

# juntando tuplas
a= (8, 6, 4, 3)
b = (8, 7, 4)
c = a + b
print(c)
# contando elementos dentro da tupla
print(c.count(8))
# pegando um index
print(c.index(8, 1))
# podemos ter dados com tipos diferentes dentro das tuplias em python
pessoa = ('isac', 39, 'M', 86.5)
print(pessoa)