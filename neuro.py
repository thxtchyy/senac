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


from tkinter import * 

pulse = Tk()
pulse.title("pulse")  
pulse.geometry("800x600")
pulse.resizable(width=FALSE, height=FALSE)

def inicial_logo():
    # CONFIGURAÇÃO PGN - LOGO
    pgn_logo = Toplevel(pulse)
    pgn_logo.title("pulse")  
    pgn_logo.geometry("800x600")
    fundo_logo = PhotoImage(file="logo_inicial.png")
    label_logo = Label(pgn_logo, image=fundo_logo)
    label_logo.place(x=0, y=0, relwidth=1, relheight=1)

    btjgr_logo = PhotoImage(file="btjogar_logo.png")
    btvtr_logo = PhotoImage(file="btvoltar_logo.png")

    btvoltar_logo = Button(pgn_logo, command=pgn_inicial, image=btvtr_logo)
    btvoltar_logo.place(x=60, y= 392, width= 302, height=98)
    
    btjogar_logo = Button(pgn_logo, command=comecar_logo, image=btjgr_logo)
    btjogar_logo.place(x=60, y= 437, width= 302, height=98)
    pgn_logo()

def comecar_logo():
    logo_1 = Toplevel(pulse)
    logo_1.title("pulse")  
    logo_1.geometry("800x600")
    quizlogo_1 = PhotoImage(file="logo_1.png")
    Label_logo1 = Label(logo_1, image=quizlogo_1)
    Label_logo1.place(x=0, y=0, relwidth=1, relheight=1)

    cor = "#E9EAEC"
    caixalg_1 = Entry(logo_1, bg=cor, font="Courier") 
    caixalg_1.place(x=60, y= 294, width= 393, height=72)
    vrfc_logo1 = Button(x= 127, y= 420, width= , height=73)
    
    resposta_logo1
    comecar_logo()

    
# IMAGENS BOTÕES JOGAR E VOLTAR

def resposta_logo1():
    resposta = entrada.get().lower()
    if resposta == "facebook":
        print("Resposta válida: )
    elif resposta == "opcao2":
        print("Resposta válida: Opção 2")
    elif resposta == "opcao3":
        print("Resposta válida: Opção 3")
    else:
        print("Resposta inválida!")

# Botão para verificar a resposta
botao_verificar = Button(text="Verificar", command=resposta_logo1)
botao_verificar.pack()
