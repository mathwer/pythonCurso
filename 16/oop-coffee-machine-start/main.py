from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

## A partir daqui o código foi escrito 

# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub 
# Documentação

bebidas = Menu()
cafeteira = CoffeeMaker()
caixa = MoneyMachine()

maquina_ligada = True

while maquina_ligada:

    opcoes = bebidas.get_items()
    pedido = input(f'Qual o seu pedido? ({opcoes}): ')
    if pedido == 'off':
        maquina_ligada = False
    
    elif pedido == 'report':
        cafeteira.report()
        caixa.report()

    elif pedido in opcoes:
        bebida = bebidas.find_drink(pedido)
        if cafeteira.is_resource_sufficient(bebida) and caixa.make_payment(bebida.cost):
            cafeteira.make_coffee(bebida)




# def pedir():
#     pedido = input('Qual o seu pedido? ')

#     if pedido in bebidas.get_items():
#         print('Vou preparar, aguarde um instante')
#         bebida = bebidas.find_drink(pedido)
#         if cafeteira.is_resource_sufficient(bebida) == False:
#             print("Desculpe, faltam recursos para fazer o café")
#             pedir()

#         else:
#             cafeteira.make_coffee(bebida)
#             caixa.make_payment(bebida.cost)
#             pedir()

#     elif pedido == 'off':
#         pass

#     elif pedido == 'report':
#         cafeteira.report()
#         pedir()

#     else:
#         print('Bebida não encontrada, tente novamente')
#         pedir()



# pedir()