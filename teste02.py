from tkinter import *

janela= Tk()
janela.title("pulse")  
janela.geometry("800x600")

# CARREGAR A IMAGEM
fundo_inicio = PhotoImage(file="pgn.inicial.png")

# CRIAÇÃO DE LABEL COM A IMAGEM
label_imagem = Label(janela, image=fundo_inicio)


# BOTÕES
    
'''IMAGEM BOTÃO - OBJETIVO'''
img_bt01 = PhotoImage(file="bt_objetivo.png")

bt01 = Button(janela, image=img_bt01)
bt01.place(x=460, y=104, width=280, height=63)

'''IMAGEM BOTÃO - NEUROBICO'''
img_bt02 = PhotoImage(file="bt_neurobico.png")

bt02 = Button(janela, image=img_bt02)
bt02.place(x=460, y=269, width=280, height=63)

'''IMAGEM BOTÃO - QUIZ'''
img_bt03 = PhotoImage(file="bt_quiz.png")

bt03 = Button(janela, image=img_bt03)
bt03.place(x=460, y=433, width=280, height=63)

def jnl_objetivo():
    
    

    

janela.mainloop()