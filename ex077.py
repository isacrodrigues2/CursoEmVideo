'''Exercício  Python 077: Crie um programa que tenha uma tupla com
várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''

palavras= ('banana', 'tomate', 'pimentao', 'alface', 'couve-flor')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=''  )
