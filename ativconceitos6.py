'''
DATA: 19/05/2023
ATIVIDADE: Faça um algoritmo que leia o salário de um funcionário,
 calcule e mostre o seu novo salário, com 15% de aumento
'''

func= input('Informe o nome do funcionário:')
salario= int(input('Informe o salário do funcionário:'))
novsalar= salario + (salario * 0.15) 
print('Agora o senhor(a)',func,'possui um salário de',novsalar,)
