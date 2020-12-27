from turtle import Turtle

DISTANCIA_MOVIMENTO = 10
POSICAO_INICIAL = ((0, 0), (-20, 0), (-40, 0))


class Cobra:

    def __init__(self):
        self.cobra = []
        self.criar_Cobra()

    def adicionar_parte(self, posicao):
        parte = Turtle(shape="square")
        parte.color('white')
        parte.penup()
        parte.shapesize(1, 1, 1)
        parte.setpos(posicao)
        parte.speed(1)
        self.cobra.append(parte)

    def criar_Cobra(self):
        for posicao in POSICAO_INICIAL:
            self.adicionar_parte(posicao)

    def crescer(self):
        self.adicionar_parte(self.cobra[-1].position())

    def cima(self):
        if self.cobra[0].heading() != 270:
            self.cobra[0].setheading(90)

    def baixo(self):
        if self.cobra[0].heading() != 90:
            self.cobra[0].setheading(270)

    def esquerda(self):
        if self.cobra[0].heading() != 0:
            self.cobra[0].setheading(180)

    def direita(self):
        if self.cobra[0].heading() != 180:
            self.cobra[0].setheading(0)

    def mover(self):
        for indice in range(len(self.cobra)-1, 0, -1):
            self.cobra[indice].goto(self.cobra[indice-1].pos())
        self.cobra[0].forward(DISTANCIA_MOVIMENTO)
