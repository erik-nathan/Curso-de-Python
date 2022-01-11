# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO,
# COM 15% DE AUMENTO.

print('============= DESAFIO 13 ==============')

s = float(input('Informe o salário: '))

newWage = (s * 15) / 100
aumento = s + newWage

print('O novo salário com aumento de 15% é: {}'.format(aumento))
