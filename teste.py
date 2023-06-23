from tkinter import *
import os

pastaPulse = os.path.dirname(__file__)

pulse = Tk()
pulse.title("PULSE")
pulse.geometry("800x600")

caminhoImagem = os.path.join(pastaPulse, "pgn.inicial.png")
imgInicial = PhotoImage(file=caminhoImagem)
l_imagem = Label(pulse, image=imgInicial)
l_imagem.pack()

pulse.mainloop()

