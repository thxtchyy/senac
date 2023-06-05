from tkinter import *

janela= Tk()
janela.title("Teste de inglês!")
janela.geometry("600x500")
janela.configure(background="#E0FFFF")

txt1=Label(janela,text="Aceita um desafio de inglês? Sim? Vamos lá!", bg="#F8F8FF", fg="#000000", font= ("Arial", 15))
txt1.place(x=20, y=80, width=600, height=30)



janela.mainloop()