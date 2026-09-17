from tkinter import *
from db import *

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


def main(a):
    ### B Novo ###
    if a == "novo":
        print("novo")

    lb = Label(frame_e_baixo, text="Insira nova tarefa", width=42, height=5, pady=15, anchor=CENTER)
    lb.grid(row=0, column=0, sticky=NSEW)

    entry = Entry(frame_e_baixo, width=15)
    entry.grid(row=1, column=0, sticky=NSEW)

    b_adicionar = Button(frame_e_baixo, text="Adicionar", width=9, height=1, bg=co6, fg=co0, font="8", anchor="center", relief=RAISED, pady=10)
    b_adicionar.grid(row=2, column=0, sticky=NSEW, pady=15)

    ### B Atualizar ###
    if a == "Atualizar":
        print("Atualizar")

############### Criando os Botões ###############

b_novo = Button(frame_e_cima, text="Novo", width=10, height=1, bg=co3, fg="white", font="5", anchor="center", relief=RAISED, command=lambda: main("novo"))
b_novo.grid(row=0, column=0, sticky=NSEW, pady=1)

b_remover = Button(frame_e_cima, text="Remover", width=10, height=1, bg=co4, fg="white", font="5", anchor="center", relief=RAISED)
b_remover.grid(row=0, column=1, sticky=NSEW, pady=1)

b_atualizar = Button(frame_e_cima, text="Atualizar", width=10, height=1, bg=co5, fg="white", font="5", anchor="center", relief=RAISED, command=lambda: main("Atualizar"))
b_atualizar.grid(row=0, column=2, sticky=NSEW, pady=1)

############### Adicionando um Label e a Listbox ###############

label = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7, padx=10, relief=RAISED, anchor=W, font=("COURIER 18 bold"), fg=co0, bg=co2)
label.grid(row=0, column=0, sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, font=("Arial 9 bold"), width=1)
listbox.grid(row=1, column=0, sticky=NSEW, pady=3)
listbox.configure(selectbackground=co3, selectforeground="white")

################# adicionando tarefas na listbox #################

def mostrar():
    tarefas = selecionar()
    for tarefa in tarefas:
        listbox.insert(END, tarefa[1])

        
mostrar()

janela.mainloop()