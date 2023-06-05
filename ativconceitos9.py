'''DATA: 19/05/2023
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
 quantidade de dias pelos quais ele foi alugado. 
Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado'''

print('Olá, você alugou um carro em nossa locadora. Responda as perguntas para o pagamento.')
dias= int(input('Quantos dias você alugou o carro: '))
km= float(input('Informe quantos Km você percorreu: '))
precodias= dias * 90
precokm= km * 0.20
total= precodias + precokm
print('O total do seu aluguel será de R$',total)