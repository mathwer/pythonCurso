from turtle import Turtle, Screen
import cobra
import time

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor('black')
tela.title('Jogo da cobrinha')
tela.tracer(0)
tela.update()
tela.listen()

cobra = cobra.Cobra()

corpo = cobra.cobra #Não foi uma boa escolha de nome da lista, então vou mudar aqui pra ajudar o resto do programa

jogo_on = True

while jogo_on:
    tela.update()
    time.sleep(0.05)
    cobra.mover()
    tela.onkeypress(cobra.cima, 'Up')
    tela.onkeypress(cobra.baixo, 'Down')
    tela.onkeypress(cobra.direita, 'Right')
    tela.onkeypress(cobra.esquerda, 'Left')




tela.exitonclick()
