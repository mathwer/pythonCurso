from tkinter import *

janela = Tk()
janela.title('Programa')
janela.minsize(width=500, height=300)

# Labels
texto = Label(text='Eu sou uma label', font=('Arial', 24))
texto.pack(side='top')  # pack coloca o objeto na tela no centro
# texto['text'] = 'Novo texto aqui'
#

# Botões


def botao_clicado():  # Criando uma função que será chamada quando o botão for clicado.
    linha = novo_input.get()
    texto['text'] = linha


botao = Button(text='Clique aqui', command=botao_clicado)
botao.pack()

# Entry => basicamente um input, mas para o tkinter

novo_input = Entry(width=10)
novo_input.pack()


janela.mainloop()
