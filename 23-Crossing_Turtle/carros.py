from turtle import Turtle
from random import choice, randint

VELOCIDADE = 5
CORES = ['blue', 'red', 'yellow', 'green', 'black', 'orange', 'purple']


class Carros():
    def __init__(self):
        self.carros = []
        self.spawn()

    def spawn(self):
        self.chance = randint(1, 6)
        if self.chance == 1:
            carro = Turtle()
            carro.setheading(180)
            carro.penup()
            carro.shape('square')
            carro.shapesize(1, 2, 1)
            carro.color(choice(CORES))
            carro.goto(400, randint(-300, 300))
            self.carros.append(carro)

    def mover(self):
        for carro in self.carros:
            carro.forward(VELOCIDADE)

    def deletar(self):
        del self
