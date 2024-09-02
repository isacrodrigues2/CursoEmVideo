# listas sãos mutavéis
num = [2, 5, 9, 1]
print(num)
# mudando um valor de uma lista
num[2] = 3
print(num)
# adicionando valores numa lista
num.append(7)
print(num)
# Organizar os valores de uma lista
num.sort()
print(num)
# Organizar os valores de uma lista ao contrário
num.sort(reverse = True)
print(num)
# remover um elemento da lista *parametro é o index
num.pop(2)
print(num)
# Inserir um elemento na lista
num.insert(2,2)
print(num)
print (f'Essa lista tem {len(num)} elementos')
# remove() remove a primeira incidência da lista
num.remove(2)
print(num)

if 4 in num:
    num.remove(4)
else: 
    print('Não achei o número 4')