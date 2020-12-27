from turtle import Turtle
from random import randint

COR = 'purple'
FORMA = 'circle'
TAMANHO = 0.5
VELOCIDADE = 'fastest'


class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FORMA)
        self.color(COR)
        self.penup()
        self.shapesize(stretch_len=TAMANHO, stretch_wid=TAMANHO)
        self.speed(VELOCIDADE)
        self.teleportar()

    def teleportar(self):
        x_random = randint(-275, 280)
        y_random = randint(-275, 260)
        self.goto(x_random, y_random)
