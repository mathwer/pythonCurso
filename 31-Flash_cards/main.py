from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


# Criando a janela principal
janela = Tk()
janela.title('Flash Cards')
janela.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Objetos do UI
card_frente = PhotoImage(file='./images/card_front.png')
card_tras = PhotoImage(file='./images/card_back.png')
correto = PhotoImage(file='./images/right.png')
errado = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800, height=525,
                bg=BACKGROUND_COLOR, highlightthickness=0)
imagem_tras = canvas.create_image(
    400, 265, image=card_frente, anchor='center')
titulo = canvas.create_text(400, 150, text='French',
                            font=('Arial', 40, 'italic'))
palavra = canvas.create_text(
    400, 263, text='palavra', font=('Arial', 60, 'bold'))

botao_certo = Button(image=correto, highlightthickness=0, borderwidth=0)
botao_erro = Button(image=errado, highlightthickness=0, borderwidth=0)


canvas.grid(column=0, row=0, columnspan=2)
botao_certo.grid(column=0, row=1)
botao_erro.grid(column=1, row=1)


janela.mainloop()
