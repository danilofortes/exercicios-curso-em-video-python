#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temp = float(input('qual a temperatura em C°: '))

fr = temp * 1.8 + 32 

print('a temperatura {} celcius é exatamente a {}F'.format(temp,fr))