import tkinter


# janela = tkinter.Tk()
# janela.title('Programa')
# janela.minsize(width=500, height=300)

# # Labels
# label = tkinter.Label(text='Eu sou uma label', font=('Arial', 24))
# label.pack(side='left')  # pack coloca o objeto na tela no centro


# janela.mainloop()

def somar_args(*args):
    i = 0
    for a in args:
        i += a

    return i


print(somar_args(1, 5, 3, 2, 5, 7, 8, 9, 3, 14, 6, 3, 5, 6))


def calcular(n, **kwargs):
    print(kwargs)

    n += kwargs['somar']
    n *= kwargs['multiplicar']

    print(n)


calcular(3, somar=3, multiplicar=4)


class Carro:
    def __init__(self, **kw):
        self.marca = kw['marca']
        self.modelo = kw['modelo']


novo_carro = Carro(marca='Nissan', modelo='HB20')
print(novo_carro.modelo)
