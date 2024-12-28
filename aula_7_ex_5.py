##escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metro = float(input('Escreva o valor em metros'))

cent = metro * 100
mili = metro * 1000

print('o número {} em metros convertido em centimetros fica {} e em milimetros fica {}'.format(metro, cent, mili))
