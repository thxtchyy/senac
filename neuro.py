# TESTE

from tkinter import *
from tkinter import font
from tkinter import Tk

def configurar_janela():
    
    janela = Tk()
    janela.title("pulse")  
    janela.geometry("800x600")
    # CARREGAR A IMAGEM
    imagem = PhotoImage(file="pgn_inicial.png")

    # CRIAÇÃO DE LABEL COM A IMAGEM
    label_imagem = Label(janela, image=imagem)
    label_imagem.place(x=0, y=0, relwidth=1, relheight=1)


    # BOTÕES
    bt01 = Button(janela, text="objetivo")
    bt01.place(x=460, y=104, width=280, height=63)
    bt01.config(bg='#90ADC6')
    bt01.config(font=('Bahnschrift SemiLight', 25))
    bt01 = Button(janela, image=imagem, bd=0, highlightthickness=0, fg='#000000')

    bt02 = Button(janela, text="neuróbico")
    bt02.place(x=460, y=269, width=280, height=63)
    bt02.config(bg='#90ADC6')
    bt02.config(font=('Bahnschrift SemiLight', 25))
    bt02 = Button(janela, image=imagem, bd=0, highlightthickness=0, fg='#000000')

    bt03 = Button(janela, text="quiz")
    bt03.place(x=460, y=433, width=280, height=63)
    bt03.config(bg='#90ADC6')
    bt03.config(font=('Bahnschrift SemiLight', 25))
    bt03 = Button(janela, image=imagem, bd=0, highlightthickness=0, fg='#000000')

    janela.mainloop()

configurar_janela()

