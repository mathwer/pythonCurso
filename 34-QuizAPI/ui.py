from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Quiz')
        self.janela.config(bg=THEME_COLOR, padx=20, pady=20)
        self.pontos = 0
        self.placar_label = Label(
            text=f'Score: {self.pontos}', bg=THEME_COLOR, fg='white', font=('Arial', 13))

        self.canvas = Canvas(width=300, heigh=250,
                             bg='white', highlightthickness=0)
        self.pergunta = self.canvas.create_text(150, 125,
                                                text='Texto', fill='black', font=('Arial', 20, 'italic'))

        self.imagem_True = PhotoImage(file='./images/true.png')
        self.imagem_False = PhotoImage(file='./images/false.png')
        self.verdadeiro = Button(
            text='', image=self.imagem_True, highlightthickness=0, borderwidth=0)
        self.falso = Button(
            text='X', image=self.imagem_False, highlightthickness=0, borderwidth=0)

        self.placar_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.verdadeiro.grid(column=0, row=2)
        self.falso.grid(column=1, row=2)

        self.janela.mainloop()
