#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
#a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('quantos km foram rodados?: '))
dia = int(input('quantos dias foram rodados?: '))

print('o preço que deverá ser pago ao aluguel de carros será de', 0.15 * km + 60 * dia)
print('dias rodados =', dia)
print('km rodados =', km)