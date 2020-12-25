import colorgram #Usado para extrair cores
import turtle
from random import choice

cores = colorgram.extract('pythonCurso/18-Turtle/projeto-colorgram/imagem.jpg', 100) #Diretório no meu PC ao usar o workspace no VSCode. Pro pycharm não de ve ser necessário 
cores_rgb = []

for cor in cores:
    r = cor.rgb.r
    b = cor.rgb.b
    g = cor.rgb.g
    cor_rgb = (r,g,b)
    cores_rgb.append(cor_rgb)

print(cores_rgb)

tartaruga = turtle.Turtle()
tartaruga.speed(0)
tartaruga.penup()
tartaruga.setpos(-250, -250)


tela = turtle.Screen()
tela.colormode(255)

def desenhar(cores, tartaruga):
    for _ in range(10):
       tartaruga.dot(20, choice(cores))
       tartaruga.forward(50)

for i in range(10):
    tartaruga.setpos(-250, (-250)+(50*i))
    desenhar(cores_rgb, tartaruga)

tartaruga.hideturtle()

tela.exitonclick()