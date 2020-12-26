from turtle import Turtle

DISTANCIA_MOVIMENTO = 10    
class Cobra:
    cobra = []
    def __init__(self):
        for i in range(3):
            parte = Turtle(shape="square")
            parte.color('white')
            parte.penup()
            parte.setpos(20*(-i), 0)
            parte.speed(1)
            self.cobra.append(parte)
        
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