#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math

num = float(input('digite um valor: '))
print (' o valor foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))