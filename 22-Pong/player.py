from turtle import Turtle

TAMANHO = 5
X_POSICAO = 500


class Player(Turtle):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero
        self.criar_jogador()
        self.transpor()

    def criar_jogador(self):
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1, 1)
        self.speed('fast')
        self.penup()

    def transpor(self):
        if self.numero == 1:
            self.setpos(-X_POSICAO, 0)

        else:
            self.setpos(X_POSICAO, 0)

    def cima(self):
        yatual = self.ycor()
        self.goto(self.xcor(), yatual + 20)

    def baixo(self):
        yatual = self.ycor()
        self.goto(self.xcor(), yatual - 20)
