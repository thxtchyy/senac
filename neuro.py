# TESTE

from tkinter import *

cor = "#E9EAEC" #azul acinzentado 

# CONFIGURAÇÃO - JANELA    
futebol = Tk()
futebol.title("pulse")  
futebol.geometry("800x600")
futebol.resizable(width=FALSE, height=FALSE)

# IMAGEM INICIAL
fundo_fut = PhotoImage(file="fut_inicial.png")
label_fut = Label(futebol, image=fundo_fut)
label_fut.place(x=0, y=0, relwidth=1, relheight=1)

# BOTÕES
img_btvoltar = PhotoImage(file="caminho/para/imagem.png")
btvoltar = Button(futebol, image=img_btvoltar)
btvoltar.place(x=60, y= 392, width= 302, height=98)

img_btjogar = PhotoImage(file="caminho/para/imagem.png")
btjogar = Button(futebol, image=img_btjogar)
btjogar.place(x=60, y= 437, width= 302, height=98)
