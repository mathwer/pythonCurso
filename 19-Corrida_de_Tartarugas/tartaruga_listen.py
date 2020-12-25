from turtle import Turtle, Screen

tartaruga = Turtle()
tela = Screen()

def praFrente():
    tartaruga.forward(10)

def virarEsquerda():
    tartaruga.left(10)

def virarDireita():
    tartaruga.right(10)

def paraTras():
    tartaruga.backward(10)

def reset():
    tartaruga.reset()

tela.listen()
tela.onkeypress(virarEsquerda, 'a')
tela.onkeypress(virarDireita, 'd')
tela.onkeypress(praFrente, 'w')
tela.onkeypress(paraTras, 's')
tela.onkeypress(reset, 'c')

tela.exitonclick()