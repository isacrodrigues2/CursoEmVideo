'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Informe um número inteiro qualquer: '))
print('Escolha uma das bases para conversão: ')
print('[1] Converter para Binário ')
print('[2] Converter para Octal')
print('[3] Converter para Hexadecimal')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O binário do número {} é {} '.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O Octal do número {} é {} '.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O Hexadecimal do número {} é {} '.format(num, hex(num)[2:]))
else:
    print('Opção invalida reinicie!')