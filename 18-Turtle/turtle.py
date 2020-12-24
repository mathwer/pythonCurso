import turtle
from random import randint, choice

tartaruga = turtle.Turtle()
tartaruga.shape('turtle')
tartaruga.color('red')


tela = turtle.Screen()
tela.colormode(255)

# ------------ Fazer um quadrado
# tartaruga.forward(100)
# tartaruga.right(90)
# tartaruga.forward(100)
# tartaruga.right(90)
# tartaruga.forward(100)
# tartaruga.right(90)
# tartaruga.forward(100)
# tartaruga.right(90)

# ---------- Fazer uma linha rasurada
# def linhaRasurada(turtle, i):
#     for i in range(i):
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()
#linhaRasurada(tartaruga, 20)

#----------- Fazer polígonos
# def poligono(turtle, l):
#     for i in range(l):
#         turtle.pencolor(randint(1,255), randint(1,255), randint(1,255))
#         turtle.forward(100)
#         turtle.right(360/l)

# poligono(tartaruga, 3)
# poligono(tartaruga, 4)
# poligono(tartaruga, 5)
# poligono(tartaruga, 6)
# poligono(tartaruga, 7)
# poligono(tartaruga, 8)

# ---------- Caminhada aleatória 

# caminhar = True
# direcoes = [0, 90, 180, 270]
# while caminhar:    
#     tartaruga.speed(10)
#     tartaruga.pencolor(randint(1,255), randint(1,255), randint(1,255))
#     tartaruga.width(5)
#     tartaruga.forward(20)
#     tartaruga.setheading(choice(direcoes))

# ---------- Spirografico

def desenho_spirografo(tamanho):
    for _ in range(int(360/tamanho)):
        tartaruga.shape('circle')
        tartaruga.pencolor(randint(1,255), randint(1,255), randint(1,255))
        tartaruga.speed(0)
        tartaruga.circle(100)
        tartaruga.setheading(tartaruga.heading() + tamanho)

desenho_spirografo(10)


tela.exitonclick()
