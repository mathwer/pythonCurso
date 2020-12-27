from turtle import Turtle

ALINHAMENTO = 'center'
FONTE = ('Courier', 100, 'bold')
POSICAO1 = (-300, 250)
POSICAO2 = (300, 250)


class Placar(Turtle):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero
        self.color('white')
        self.hideturtle()
        self.penup()
        self.pontos = 0
        self.mover()
        self.mostrar_pontos()

    def mostrar_pontos(self):
        self.clear()
        self.write(self.pontos, align=ALINHAMENTO, move=False, font=FONTE)

    def mover(self):
        if self.numero == 1:
            self.setpos(POSICAO1)
        else:
            self.setpos(POSICAO2)
