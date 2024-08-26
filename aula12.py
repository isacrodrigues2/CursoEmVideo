nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Isac':
    print('Que nome bonito!')
elif nome == 'isac':
    print('faltou a maíuscula no ínicio')
elif nome == 'ISAC':
    print('Para de gritar!!')
elif nome == 'Maria' or nome == 'João':
    print('Seu nome é bem comum no Brasil')
else:
    print('que nome normal')
print('Tenha um bom dia {}'.format(nome))