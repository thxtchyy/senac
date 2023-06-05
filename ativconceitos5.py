''' 
data: 19/05/2023
ATIVIDADE: Crie um programa que leia o preço de um produto, calcule e mostre o seu 
 PREÇO PROMOCIONAL, com 5% de desconto
'''

nmr=float(input('Qual o preço do produto?'))
desconto = nmr - (nmr * 0.05)
print('O valor do produto com o desconto de 5 porcento será de',desconto)