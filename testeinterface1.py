# Para importar o Tkinter para o seu projeto basta digitar
from tkinter import *

# PARA CRIAR UMA NOVA INSTÂNCIA -> CRIAR VARIÁVEL. 
# variável: Janela; instância: Tk()
janela = Tk()

# o label deve estár vinculado a instância.
Label(janela, text="olá, mundo").pack()

# faz a janela continuar aberta.
janela.mainloop() 
