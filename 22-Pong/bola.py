from turtle import Turtle
from random import randint, randrange


class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fast')
        self.penup()
        self.inicio()
        self.x_move = 10
        self.y_move = 10

    def mover(self):
        novo_x = self.xcor() + self.x_move
        novo_y = self.ycor() + self.y_move
        self.goto(novo_x, novo_y)

    def inicio(self):
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10

    def bater_parede(self):
        self.y_move *= -1

    def bater_player(self):
        self.x_move *= -1
