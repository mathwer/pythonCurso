import turtle
import pandas

imagem = 'blank_states_img.gif'
tela = turtle.Screen()
tela.screensize()
tela.title('Estados dos EUA')
tela.addshape(imagem)

turtle.shape(imagem)

# Pegar as coordenadas, elas já estão no arquivo csv
# def pegar_coordenadas(x, y):
#     print(x, y)

# turtle.onscreenclick(pegar_coordenadas)


# Configuração dos dados

estados_data = pandas.read_csv('50_states.csv')
estados_nome = estados_data['state']


# Configuração da Classe que será o nome dos estados
FONTE = ('Courier', 8, 'normal')


class Estado(turtle.Turtle):
    def __init__(self, estado, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.estado = estado
        self.x = x
        self.y = y
        self.goto(self.x, self.y)

        self.write(estado, align='center', move=False, font=FONTE)


# Configuração do Jogo
estados_certos = []
while len(estados_certos) < 50:
    tentativa_estado = tela.textinput(
        title=f'{len(estados_certos)}/50 descobertos: ', prompt='Você se lembra o nome de algum estado?')
    for estado in estados_nome:
        if tentativa_estado.lower() == estado.lower():
            linha = estados_data[estados_data['state'] == estado]
            acerto = Estado(estado, int(linha.x), int(linha.y))
            if estado not in estados_certos:
                estados_certos.append(estado)

    if tentativa_estado.lower() == 'exit':

        # Criar um arquivo com os estados restantes
        estados_restantes = [
            estado for estado in estados_nome if estado not in estados_certos]
        estados_restantes = pandas.DataFrame(estados_restantes)
        estados_restantes.to_csv('Estados_para_aprender.csv')

        # Sair do programa
        break


turtle.mainloop()
