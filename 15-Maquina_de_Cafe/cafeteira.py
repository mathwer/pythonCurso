#Cafeteira nova
def cafeteira(): 
    agua = 1000
    cafe = 1000
    leite = 1000
    dinheiro = 5.00 

    def ordem():
        nonlocal agua
        nonlocal cafe
        nonlocal leite
        nonlocal dinheiro
        pedido = input("Qual o seu pedido? Expresso / Latte / cappuccino ")

        if pedido == 'off':
            print("Desligando a máquina")            
        
        elif pedido == "report":
            print("Água = "+ str(agua)+'ml')
            print("Café = "+str(cafe)+'g')
            print('Leite = '+str(leite)+'ml')
            print('Dinheiro = $' + str(dinheiro))
        
        elif pedido == 'Expresso' or pedido == "expresso":
            checarItens(50, 18, 0)
            inserirDinheiro(1.5)
            print('Aqui está seu expresso')
            ordem()

        elif pedido == 'Latte' or pedido == 'latte':
            checarItens(200, 24, 150)
            inserirDinheiro(2.5)
            print('Aqui está seu latte')
            ordem()

        elif pedido == 'Cappuccino' or pedido == 'cappuccino':
            checarItens(250, 24, 100)
            inserirDinheiro(1.5)
            print('Aqui está seu Cappuccino')
            ordem()


        elif pedido == 'reabastecer':
            agua += 500
            cafe += 500
            leite += 500
            print('A máquina foi reabastecida.')
            ordem()

        else:
            print('Comando não reconhecido, por favor, tente novamente.')
            ordem()


    def checarItens(a, c, l):
        nonlocal agua
        nonlocal cafe
        nonlocal leite

        if a > agua:
            print('Desculpe, água insuficiente')
        elif c > cafe:
            print('Desculpe, café insuficiente')
        elif l > leite:
            print('Desculpe, leite insuficiente')
        else:
            print("Preparando sua bebida")
            agua -= a
            cafe -= c  
            leite -= l


    def inserirDinheiro(preco):
        nonlocal dinheiro
        print('Você precisa inserir $' + str(preco))
        um = float(input("Quantas moedas de 1¢?"))*0.01
        cinco = float(input("Quantas moedas de 5¢?"))*0.05
        dez = float(input("Quantas moedas de 10¢?"))*0.1
        vinteCinco = float(input("Quantas moedas de 25¢?"))*0.25
        cinquenta = float(input("Quantas moedas de 50¢?"))*0.5
        total = um + cinco + dez + vinteCinco + cinquenta

        if total < preco:
            print('Dinheiro Insuficiente, reiniciando o pedido')
            ordem()
        elif total == preco:
            print("Dinheiro aceito, aguarde seu pedido")
            dinheiro += total
        elif total > preco:
            print("Aqui está seu troco de $" + str(round(total - preco, 2))+ '. Aguarde seu pedido.' )
            dinheiro += round(total - preco, 2)

    ordem()
    

cafeteira()