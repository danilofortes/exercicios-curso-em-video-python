#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('qual é o valor do cateto oposto?: '))
ca = float(input('qual é o valor do cateto adjacente?: '))
hi = math.hypot(co, ca)
print('com o cateto oposto sendo {} e o cateto adjacente sendo{}, logo, a sua hipotenusa é {}'.format(co,ca,hi))