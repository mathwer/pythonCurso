from turtle import Turtle, Screen
from carros import Carros
from tartaruga import Jogador
from placar import Placar
import time
from threading import Timer  # para dar o delay dos carros

# Configurando a tela
tela = Screen()
tela.screensize(600, 600)
tela.tracer(0)


# Instanciando o player, o placar e a lista de carros
jogador = Jogador()
carros = Carros()
placar = Placar()

# Esperando os comandos
tela.listen()
tela.onkeypress(jogador.mover, 'w')


# Configurando o jogo
jogo_on = True
velocidade = 5
while jogo_on:
    time.sleep(0.1)
    tela.update()

    carros.spawn()

    for carro in carros.carros:
        carro.forward(velocidade)
        if carro.distance(jogador) <= 30:
            placar.gameOver()
            tela.update()
            jogo_on = False

    if jogador.ycor() >= 280:
        placar.level += 1
        placar.atualizar()
        jogador.inicio()
        velocidade *= 1.1


tela.exitonclick()
