from tkinter import *

janela = Tk()
janela.title('Programa')
janela.minsize(width=500, height=300)
janela.config(padx=20, pady=20)


def botao_clicado():  # Criando uma função que será chamada quando o botão for clicado.
    linha = novo_input.get()
    texto['text'] = linha


texto = Label(text='Texto normal', font=('Arial', 24))
# texto.pack(side='top')
# Além do pack, pode ser utilizado também place para criação precisa de pontos e grid para dividir a tela em setores.
# texto['text'] = 'Novo texto aqui'
# texto.place(x=100, y=200)
texto.grid(column=0,  row=0)


# O modelo grid é relativo aos outros elementos que estão no tkinter. Por isso, caso você só tenha um elemento, ele será posicionado no topo esquerdo.


botao = Button(text='Clique aqui', command=botao_clicado)
# botao.pack()  # Pack sempre começa do topo e coloca os objetos abaixo dos anteiores caso não tenha um parametro
botao.grid(column=1, row=1)

novo_botao = Button(text='Novo Botão', command=botao_clicado)
novo_botao.grid(column=3, row=0)

# Entry => basicamente um input, mas para o tkinter

novo_input = Entry(width=10)
# novo_input.pack()
novo_input.grid(column=4, row=3)


# Existem outros objetos que podem ser criados, como spinbox, scale, checkbox, radiobuttons, listbox

janela.mainloop()
