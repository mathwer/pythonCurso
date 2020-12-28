from turtle import Turtle
FONTE = ('Courier', 24, "normal")


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.atualizar()

    def atualizar(self):
        self.goto(-320, 350)
        self.clear()
        self.write(f'Nível atual: {self.level}',
                   False, align='center', font=FONTE)

    def gameOver(self):
        self.goto(0, 0)
        self.write('Game Over!', False, 'center', font=FONTE)
