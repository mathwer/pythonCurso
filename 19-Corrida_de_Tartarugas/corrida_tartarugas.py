from turtle import Turtle, Screen
from random import randint

t1 = Turtle(shape='turtle')
t2 = Turtle(shape='turtle')
t3 = Turtle(shape='turtle')
t4 = Turtle(shape='turtle')
t5 = Turtle(shape='turtle')
t6 = Turtle(shape='turtle')


tela = Screen()
tela.setup(width=500, height=400)

t1.color('blue')
t2.color('yellow')
t3.color('red')
t4.color('green')
t5.color('brown')
t6.color('orange')

corrida = False


aposta = tela.textinput(title='Faça sua aposta', prompt='Escolha a cor da tartaruga vencedora (red, yellow, blue, green, orange, brown)')


tartarugas = [t1,t2,t3,t4,t5,t6]
h = -125 
for t in    tartarugas:
    t.penup()
    t.goto(-230, h)
    h += 50

if aposta: 
    corrida = True

while corrida:
    for t in tartarugas:    
        if t.xcor() > 225:
            corrida = False
            vencedor = t.pencolor()
            if aposta.lower() == vencedor.lower():
                print('Parabéns, sua tartaruga é a campeã :DDD')
            else:
                print(f'Que pena, a tartaruga {t.pencolor()} é a vencedora :/')
 
        distancia = randint(0, 10)
        t.forward(distancia)
        

