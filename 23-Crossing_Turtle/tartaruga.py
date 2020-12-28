from turtle import Turtle


class Jogador(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.inicio()

    def mover(self):
        self.forward(10)

    def inicio(self):
        self.goto(0, -350)
