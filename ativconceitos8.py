'''DATA: 19/05/2023
ATIVIDADE: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira 
(em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.'''

cart= float(input('Informe quantos reais você possui em sua carteira:'))
dolar= cart / 3.45
print('Você possui',dolar,'dólares em sua carteira.')