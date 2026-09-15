from tkinter import *

############### Cores usadas ###############

co0 = "#e0e0e0"   # texto claro
co1 = "#121212"   # fundo
co2 = "#1e1e1e"   # painéis
co3 = "#3b82f6"
co4 = "#ef4444"
co5 = "#22c55e"
co6 = "#2c2c2c"

############### Criando Janela Principal ###############

janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x225')
janela.title('To-Do App')
janela.configure(background=co1)

############### Dividindo a Janela em Duas Partes ###############

frame_esquerda = Frame(janela, width=300, height=200, bg=co2, relief=RAISED)
frame_esquerda.grid(row=0, column=0, sticky=NSEW)
frame_direita = Frame(janela, width=200, height=250, bg=co2, relief=RAISED)
frame_direita.grid(row=0, column=1, sticky=NSEW)

############### Dividindo o Frame Esquerdo em Cima e Baixo ###############

frame_e_cima = Frame(frame_esquerda, width=300, height=50, bg=co2, relief=RAISED)
frame_e_cima.grid(row=0, column=0, sticky=NSEW)

frame_e_baixo = Frame(frame_esquerda, width=300, height=150, bg=co2, relief=RAISED)
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)