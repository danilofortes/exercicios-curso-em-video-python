#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la.
#sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('coloque a altura da sua parede em metros: '))
largura = float(input('agora coloque a largura da sua parede em metros: '))

areaquad = altura * largura
tinta = areaquad / 2

print('a sua parede de {} metros quadrados irá precisar de {} litros de tinta'.format(areaquad, tinta))