#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario  = float(input('digite seu salário: '))
aumento = 0.15 * salario + salario
print('o sálario de {} com 15% de aumento é {}'.format(salario, aumento))