'''
DATA: 19/05/2023
ATIVIDADE: Faça um algoritmo que leia a largura e altura de uma parede, 
calcule e mostre a área a ser pintada e a quantidade de tinta necessária 
para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
'''

lar= float(input('Digite a largura da sua parede:'))
alt= float(input('Digite a largura da sua parede:'))
calc= (lar * alt) / 2
print('A quantidade de litros necessária para pintar essa área, seria de',calc,'litros')