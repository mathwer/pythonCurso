from turtle import Turtle

TAMANHO_TELA = -400


class Divisoria(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.pensize(2)

    def tracejar(self):
        self.goto(0, TAMANHO_TELA)
        self.setheading(90)
        i = 0
        while i < 40:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            i += 1
