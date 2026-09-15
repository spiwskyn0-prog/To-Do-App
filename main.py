from tkinter import *

################# Cores usadas no projeto ##############

co0 = "#e0e0e0"   # texto claro
co1 = "#121212"   # fundo
co2 = "#1e1e1e"   # painéis
co3 = "#3b82f6"
co4 = "#ef4444"
co5 = "#22c55e"
co6 = "#2c2c2c"

################# Criando Janela Principal #################

janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x225')
janela.title('To-Do App')
janela.configure(background=co1)