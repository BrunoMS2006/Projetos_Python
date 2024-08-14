import math
x=input('Digite  algo:')
print('É um numero?', x.isnumeric())
print('É um alfanumerico (numeros e letras)?', x.isalnum())
print('É um alfabético? (letras?)', x.isalpha())
print('esta em minusculo?', x.islower())
print('esta em maiusculo?', x.isupper())
print('É somente espaço?', x.isspace())
print('esta capitalizado (possui maisculas e minusculas?)3,14', x.istitle())