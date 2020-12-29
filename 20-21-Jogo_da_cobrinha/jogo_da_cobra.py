from turtle import Turtle, Screen
import cobra
import time
import comida
import placar
import borda

# Configuração da tela
tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor('black')
tela.title('Jogo da cobrinha')

# Colocando tracer no 0 e fazendo a tela dar o update
tela.tracer(0)
tela.update()


# Instancias da cobra, da comida e do placar
borda = borda.Borda()
cobra = cobra.Cobra()
comida = comida.Comida()
placar = placar.Placar()


# Comandos que a tela vai esperar receber
tela.listen()
tela.onkeypress(cobra.cima, 'Up')
tela.onkeypress(cobra.baixo, 'Down')
tela.onkeypress(cobra.direita, 'Right')
tela.onkeypress(cobra.esquerda, 'Left')


# Iniciando o jogo
jogo_on = True

while jogo_on:
    tela.update()
    time.sleep(0.05)
    cobra.mover()

    # Comeu comida
    if cobra.cobra[0].distance(comida) < 15:
        comida.teleportar()
        placar.pontos += 1
        placar.atualizar()
        cobra.crescer()

    # Comida spawna no corpo da cobra
    for parte in cobra.cobra[1:]:
        if parte.distance(comida) < 15:
            comida.teleportar()

    # Bateu com as paredes
    if cobra.cobra[0].xcor() > 280 or cobra.cobra[0].xcor() < -280 or cobra.cobra[0].ycor() > 265 or cobra.cobra[0].ycor() < -280:
        placar.reset()
        cobra.reset()

    # Colidiu com a cauda
    for parte in cobra.cobra[1:]:
        if cobra.cobra[0].distance(parte) < 7:
            placar.reset()

tela.exitonclick()
