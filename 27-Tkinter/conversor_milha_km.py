from tkinter import *

janela = Tk()
janela.title('Conversor milha para km')
janela.minsize()
janela.config(padx=20, pady=20)

FONTE = ('Courier', 14)


def transformar():
    kms = round(int(milhas.get()) * 1.6, 2)
    conversao['text'] = kms


texto1 = Label(text='é igual a', font=FONTE)
texto1.grid(column=0, row=1)

texto2 = Label(text='Milhas', font=FONTE)
texto2.grid(column=2, row=0)

texto3 = Label(text='Km', font=FONTE)
texto3.grid(column=2, row=1)

conversao = Label(text=0, font=FONTE)
conversao.grid(column=1, row=1)

milhas = Entry(font=FONTE, justify='center', width=10)
milhas.insert(END, string='0')
milhas.grid(column=1, row=0)

botao = Button(text='Calcule!', command=transformar, font=FONTE)
botao.grid(column=1, row=2)


janela.mainloop()
