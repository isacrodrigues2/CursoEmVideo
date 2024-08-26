from curses.ascii import *

a = input('Digite Algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maíusculas? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())


