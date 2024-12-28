#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input('coloque o valor que possuí em sua carteira: '))

dolar = real * 0.16

print('você possuí {} reais, convertendo em dólar são {} dólares'.format(real, dolar))