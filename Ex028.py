from random import randint
from time import sleep

print('=-=' * 20)
print("Pensei em um número de 0 a 5, adivinhe qual é...")
print('=-=' * 20)
num = randint(0,5) # Faz o computador "pensar em um número"
n = int(input('Digite seu palpite: ')) # insere o palpite do usuário
print('Processando...')
sleep(2)
if num == n: # compara o número que o computador pensou com o número que o usuário digitou
    print("Você acertou!")
else:
    print("Você errou eu estava pentando no número {}".format(num))