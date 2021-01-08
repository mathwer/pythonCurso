from tkinter import *
from tkinter import messagebox as mb
from random import randint, choice, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gerar_senha():
    senha_entry.delete(0, END)
    password_list_lt = [choice(letters) for i in range(randint(8, 10))]
    password_list_num = [choice(numbers) for i in range(randint(2, 4))]
    password_list_spc = [choice(symbols) for i in range(randint(2, 4))]
    password_list = password_list_lt + password_list_spc + password_list_num

    shuffle(password_list)

    senha = ''.join(password_list)

    senha_entry.insert(0, senha)
    janela.clipboard_clear()
    janela.clipboard_append(senha)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def salvar_dados():
    email = email_entry.get()
    site = site_entry.get()
    senha = senha_entry.get()
    # frase = f' {site} || {email} || {senha} \n '
    novos_dados = {site: {
        'User': email,
        'Senha': senha
    }}

    if email and site and senha:
        confirmacao = mb.askokcancel(
            'Confirmação', f'Por favor, confira os dados para o site {site}. \n  Email: {email} \n Senha: {senha} \n Posso salvar os dados?')
        if confirmacao:
            # with open('senhas.txt', 'a') as senhas: #Trocado para usar um arquivo .json
            # senhas.write(frase)
            try:
                with open('senhas.json', 'r') as senhas:
                    dados = json.load(senhas)

            except FileNotFoundError:
                with open('senhas.json', 'w') as senhas:
                    json.dump(novos_dados, senhas, indent=4)

            else:
                dados.update(novos_dados)
                with open('senhas.json', 'w') as senhas:
                    json.dump(dados, senhas, indent=4)

            # Se for usar vários e-mails, pode descomentar a linha abaixo, mas se for usar apenas um e-mail, é interessante deixa-la
            # email_entry.delete(0, END

            site_entry.delete(0, END)
            senha_entry.delete(0, END)
            site_entry.focus()
    else:
        mb.showerror('Erro', 'Por favor, preencha todos os campos.')

# ---------------------------- Site Search ------------------------------- #


def procurar_site():
    site_tela = site_entry.get()
    try:
        with open('senhas.json', 'r') as senhas:
            dados = json.load(senhas)
    except:
        mb.showerror('Erro', 'Nenhuma senha encontrada.')

    else:
        encontrados = 0
        for site in dados:
            if site_tela.lower() == site.lower():
                valores = list(dados[site].values())
                mb.showinfo(f'Dados {site}',
                            f"Usuário: {valores[0]} \nSenha: {valores[1]}")
                encontrados += 1
        if encontrados == 0:
            mb.showinfo('Não encontrado',
                        f'Desculpe, nenhum site com o nome {site_tela} foi encontrado')


# ---------------------------- UI SETUP ------------------------------- #
janela = Tk()
janela.title = ('Organizador de Senhas')
janela.configure(padx=50, pady=50)

imagem = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=imagem)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
site = Label(text='Website: ')
email = Label(text='E-mail/Usuário:')
senha = Label(text='Senha: ')
site.grid(row=1, column=0)
email.grid(row=2, column=0)
senha.grid(row=3, column=0)

# Entrys
site_entry = Entry(width=33)
site_entry.focus()
email_entry = Entry(width=35)

# Aqui pode trocar pelo email mais usado
email_entry.insert(0, 'meu_email@email.com')
senha_entry = Entry(width=33)

site_entry.grid(row=1, column=1, sticky="EW")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
senha_entry.grid(row=3, column=1, sticky="W")

# Botoes
botao_gerar = Button(text='Gerar', command=gerar_senha)
botao_adicionar = Button(text='Adicionar conta',
                         width=30, command=salvar_dados)
bota_procurar = Button(text='Procurar', width=30, command=procurar_site)

botao_gerar.grid(row=3, column=2, sticky='EW')
botao_adicionar.grid(row=4, column=1, columnspan=2, sticky="EW")
bota_procurar.grid(row=1, column=2, sticky="EW")

janela.mainloop()
