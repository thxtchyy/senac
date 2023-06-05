# Para importar o Tkinter para o seu projeto basta digitar
from tkinter import *

# Agora, para criar uma nova instância, crie uma variável 
# com o nome "janela" e atribua a ela a instância usando "Tk()":
janela = Tk()

# Para adicionar algum texto, crie o Label, vincule ele a 
# variável janela e adicione o texto de seu interesse. 
# (Não esqueça de adicionar o gerenciador de layout)
Label(janela, text="olá, mundo").pack()

# E mande a aplicação ser executada
janela.mainloop() 