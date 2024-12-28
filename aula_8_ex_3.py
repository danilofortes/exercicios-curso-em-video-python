#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = float(input('qual é o ângulo?: '))
seno = sin(radians(angulo))

print('o ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

coss = cos(radians(angulo))

print('o ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, coss))

tangente = tan(radians(angulo))

print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
