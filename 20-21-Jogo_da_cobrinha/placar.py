from turtle import Turtle

ALINHAMENTO = 'center'
FONTE = ('Courier', 20, 'bold')

with open('recorde.txt') as txt:  # Usando dessa forma, o arquivo é fechado automaticamente
    recorde_atual = int(txt.read())


class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.pontos = 0
        self.recorde = recorde_atual
        self.goto(0, 265)
        self.color('white')
        self.hideturtle()
        self.atualizar()

    def atualizar(self):
        self.clear()
        self.write(f'Pontos: {self.pontos} Recorde: {self.recorde}', move=False,
                   align=ALINHAMENTO, font=FONTE)

    def reset(self):
        if self.recorde <= self.pontos:
            self.recorde = self.pontos
            with open('recorde.txt', mode='w') as txt:
                txt.write(str(self.recorde))

        self.pontos = 0
        self.atualizar()

    def gameOver(self):
        self.goto(0, 0)
        self.write('Game Over!', move=False, align=ALINHAMENTO, font=FONTE)
