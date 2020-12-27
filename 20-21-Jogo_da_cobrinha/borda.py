from turtle import Turtle

TAMANHO = 280


class Borda(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-TAMANHO, -TAMANHO)
        self.pendown()
        self.goto(-TAMANHO, 270)
        self.goto(TAMANHO, 270)
        self.goto(TAMANHO, -TAMANHO)
        self.goto(-TAMANHO, -TAMANHO)
