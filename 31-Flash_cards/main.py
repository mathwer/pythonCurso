from tkinter import *
import pandas
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"

# ------------  Pegando as palavras  ------------------
try:
    data = pandas.read_csv('./data/para_aprender.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')

data_dict = data.to_dict(orient='records')
par = choice(data_dict)

# -----------  Mostrando a Resposta ----------------------


def mostrar_resposta():
    global par
    palavra_en = par['English']
    canvas.itemconfig(palavra_da_vez, text=palavra_en, fill='white')
    canvas.itemconfig(titulo, text='English', fill='white')
    canvas.itemconfig(imagem, image=card_tras)
    par = choice(data_dict)

# -----------  Trocando a palavra com os botões ----------------


def proxima_palavra_erro():
    global virar
    janela.after_cancel(virar)
    canvas.itemconfig(imagem, image=card_frente)
    palavra_fr = par['French']
    canvas.itemconfig(palavra_da_vez, text=palavra_fr, fill='black')
    canvas.itemconfig(titulo, text='French', fill='black')
    virar = janela.after(3000, mostrar_resposta)


def proxima_palavra_acerto():
    proxima_palavra_erro()
    data_dict.remove(par)
    palavras_para_aprender = pandas.DataFrame(data_dict)
    palavras_para_aprender.to_csv('./data/para_aprender.csv', index=False)

# --------------- Tirar as palavras que já sabe -----------------------


# Criando a janela principal
janela = Tk()
janela.title('Flash Cards')
janela.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Objetos do UI
card_frente = PhotoImage(file='./images/card_front.png')
card_tras = PhotoImage(file='./images/card_back.png')
correto = PhotoImage(file='./images/right.png')
errado = PhotoImage(file='./images/wrong.png')

# Canvas
canvas = Canvas(width=800, height=525,
                bg=BACKGROUND_COLOR, highlightthickness=0)
imagem = canvas.create_image(
    400, 265, image=card_frente, anchor='center')
titulo = canvas.create_text(400, 150, text='French',
                            font=('Arial', 40, 'italic'))
palavra_da_vez = canvas.create_text(
    400, 263, text='palavra', font=('Arial', 60, 'bold'))

# Botões
botao_certo = Button(image=correto, highlightthickness=0,
                     borderwidth=0, command=proxima_palavra_acerto)
botao_erro = Button(image=errado, highlightthickness=0,
                    borderwidth=0, command=proxima_palavra_erro)

# Colocando no grid
canvas.grid(column=0, row=0, columnspan=2)
botao_certo.grid(column=1, row=1)
botao_erro.grid(column=0, row=1)


# Chamando as funções
virar = janela.after(3000, mostrar_resposta)
proxima_palavra_erro()

janela.mainloop()
