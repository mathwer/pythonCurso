from turtle import Turtle, Screen
from random import randint
import traco
import player
import time
import bola
import placar

# Configurando a tela
tela = Screen()
tela.setup(width=1200, height=800)
tela.bgcolor('black')
tela.title('Pong')
tela.tracer(0)
tela.update()
# Instanciar bola, players e Placar
player1 = player.Player(1)
player2 = player.Player(2)
traco = traco.Divisoria()
bola1 = bola.Bola()
placar1 = placar.Placar(1)
placar2 = placar.Placar(2)
traco.tracejar()
tela.update()

# Esperar pelos comandos e ativa-los
tela.listen()
tela.onkeypress(player1.cima, 'w')
tela.onkeypress(player2.cima, 'Up')
tela.onkeypress(player1.baixo, 's')
tela.onkeypress(player2.baixo, 'Down')


jogo_on = True
velocidade = 0.05

while jogo_on:
    tela.update()
    time.sleep(velocidade)
    bola1.mover()

    # Mudar a diração da bola quando bater em alguma coisa
    if bola1.ycor() > 380 or bola1.ycor() < -380:
        bola1.bater_parede()

    if bola1.distance(player1) < 90 and bola1.xcor() == -490 or bola1.distance(player2) < 90 and bola1.xcor() == 490:
        print('bateu')
        bola1.bater_player()
        velocidade *= 0.85

    # Detectar se ocorreu um ponto
    if bola1.xcor() == 600:
        placar1.pontos += 1
        placar1.mostrar_pontos()
        bola1.inicio()
        time.sleep(1)
        velocidade = 0.05

    if bola1.xcor() == -600:
        placar2.pontos += 1
        placar2.mostrar_pontos()
        bola1.inicio()
        time.sleep(1)
        velocidade = 0.05

tela.exitonclick()
