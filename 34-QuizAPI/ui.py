from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.janela = Tk()
        self.janela.title('Quiz')
        self.janela.config(bg=THEME_COLOR, padx=20, pady=20)
        self.placar_label = Label(
            text=f'Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 13))

        self.canvas = Canvas(width=300, heigh=250,
                             bg='white', highlightthickness=0)
        self.pergunta = self.canvas.create_text(150, 125, width=280,
                                                text='Texto', fill='black', font=('Arial', 20, 'italic'))

        self.imagem_True = PhotoImage(file='./images/true.png')
        self.imagem_False = PhotoImage(file='./images/false.png')
        self.verdadeiro = Button(
            text='', image=self.imagem_True, highlightthickness=0, borderwidth=0, command=self.resposta_true)
        self.falso = Button(
            text='', image=self.imagem_False, highlightthickness=0, borderwidth=0, command=self.resposta_false)

        self.placar_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.verdadeiro.grid(column=0, row=2)
        self.falso.grid(column=1, row=2)

        self.pegar_proxima_pergunta()

        self.janela.mainloop()

    def pegar_proxima_pergunta(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.placar_label.config(text=f'Score: {self.quiz.score}')
            texto = self.quiz.next_question()
            self.canvas.itemconfig(self.pergunta, text=texto)
        else:
            self.canvas.itemconfig(self.pergunta,
                                   text=f'Acabou! Seu placar final é {self.quiz.score}!')
            self.verdadeiro.config(state='disabled')
            self.falso.config(state='disabled')

    def resposta_true(self):
        self.feedback(self.quiz.check_answer(True))

    def resposta_false(self):
        self.feedback(self.quiz.check_answer(False))

    def feedback(self, esta_certo):
        if esta_certo:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')

        self.janela.after(500, self.pegar_proxima_pergunta)
