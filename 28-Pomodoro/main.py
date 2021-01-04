from tkinter import *

# ---------------------------- CONSTANTES ------------------------------- #
ROSA = "#e2979c"
VERMELHO = "#e7305b"
VERDE = "#9bdeac"
AMARELO = "#f7f5dd"
FONT_NAME = "Courier"
TEMPO_PRODUTIVO = 25
INTERVALO_CURTO = 5
INTERVALO_LONGO = 20
CHECKMARK = '✓'

# ---------------------------- TIMER RESET ------------------------------- #
temporizador = None
repeticoes = 0


def reset_timer():
    global repeticoes
    repeticoes = 0
    janela.after_cancel(temporizador)
    canvas.itemconfig(contador, text='00:00')
    check.config(text='')
    botao_inicio.config(state='normal')


# ---------------------------- TIMER MECHANISM ------------------------------- #


def iniciar_contador():
    botao_inicio.config(state='disabled')
    global repeticoes

    repeticoes += 1
    if repeticoes % 8 == 0:
        count_down(INTERVALO_LONGO * 60)
        titulo.config(text='Intervalo', fg=VERMELHO)

    elif repeticoes % 2 == 0:
        count_down(INTERVALO_CURTO * 60)
        titulo.config(text='Intervalo', fg=ROSA)

    else:
        count_down(TEMPO_PRODUTIVO * 60)
        titulo.config(text='Trabalhando', fg=VERDE)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global temporizador
    minutos = str(count//60).zfill(2)
    segundos = str(count % 60).zfill(2)
    canvas.itemconfig(contador, text=f'{minutos}:{segundos}')
    if count > 0:
        temporizador = janela.after(1000, count_down, count-1)
    else:
        iniciar_contador()
        check.config(text=(CHECKMARK * int(repeticoes/2)))


# ---------------------------- UI SETUP ------------------------------- #

janela = Tk()
janela.title('Pomodoro')
janela.configure(bg=AMARELO, padx=100, pady=50)

imagem = PhotoImage(file='tomato.png')

canvas = Canvas(width=200, height=224, bg=AMARELO, highlightthickness=0)
canvas.create_image(100, 112, image=imagem)
contador = canvas.create_text(100, 130, text='00:00', fill='white',
                              font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

titulo = Label(text='Timer')
titulo.config(fg=VERDE, width=11, font=(FONT_NAME, 40, 'bold'), bg=AMARELO)
titulo.grid(column=1, row=0)

check = Label(text='', fg=VERDE, bg=AMARELO,
              font=(FONT_NAME, 20, 'bold'))
check.grid(column=1, row=3)

botao_inicio = Button(text='Iniciar', fg=VERDE,
                      bg=AMARELO, highlightthickness=0, command=iniciar_contador)
botao_inicio.grid(column=0, row=2)

botao_reset = Button(text='Reset', fg=VERDE, bg=AMARELO,
                     highlightthickness=0, command=reset_timer)
botao_reset.grid(column=2, row=2)


janela.mainloop()
