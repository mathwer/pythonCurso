from turtle import Turtle

ALINHAMENTO = 'center'
FONTE = ('Courier', 20, 'bold')


class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.pontos = 0
        self.goto(0, 265)
        self.color('white')
        self.hideturtle()
        self.atualizar()

    def atualizar(self):
        self.clear()
        self.write(f'Pontos: {self.pontos}', move=False,
                   align=ALINHAMENTO, font=FONTE)

    def gameOver(self):
        self.goto(0, 0)
        self.write('Game Over!', move=False, align=ALINHAMENTO, font=FONTE)
