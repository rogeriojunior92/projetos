import os
from time import sleep

lista_carpadio = []

menu_completo = ("Calabresa", 25.00, "Mussarela", 22.00, "Palmito", 30.00, "Frango c/ Caputiry", 23.00, "Coca-Cola", 6.00,
                 "Pepsi", 5.00, "Suco", 3.00, "Cerveja", 7.50, "Pudim", 8.00, "Bolo", 10.00, "Banana Split", 15.00, "Gelatina", 5.00)

cardapio = {
    "pizza":{
        "100": ["Calabresa", 25.00],
        "101": ["Mussarela", 22.00],
        "102": ["Palmito", 30.00],
        "103": ["Frango c/ Caputiry", 23.00]
    },

    "bebida": {
        "110": ["Coca-Cola", 6.00],
        "111": ["Pepsi", 5.00],
        "112": ["Suco", 3.00],
        "113": ["Cerveja", 7.50]
    },

    "sobremesa": {
        "120": ["Pudim", 8.00],
        "121": ["Bolo", 10.00],
        "122": ["Banana Split", 15.00],
        "123": ["Gelatina", 5.00],
    }
}   


def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(TypeError, ValueError):
            sleep(0.5)
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except(KeyboardInterrupt):
            sleep(0.5)
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num


def resposta():
    while True:
        resp = input("Deseja escolher algo mais? [S/N] ").upper()[0]
        if resp in "SN":
            break
    if resp == "N":
        print("Saindo da Tela.")


def carpadio_completo():
    os.system("cls")
    titulo("CARDAPIO COMPLETO".center(50))
    for c in range(0, len(menu_completo), 2):
        print(f"{menu_completo[c]:.<40} R$ {menu_completo[c+1]:>6.2f}")


def carpazio_pizza():
    os.system
    total_pizza = 0
    titulo("CARDÁPIO DE PIZZA".center(50))
    print("1 - Calabresa\n2 - Mussarela\n3 - Palmito\n4 - Frango c/ Caputiry\n5 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para escolehr a Pizza: ")
    if opcao == 1:
        total_pizza += cardapio['pizza']["100"][1]
        lista_carpadio.append(total_pizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Calabresa R$ {:.2f}".format(cardapio['pizza']["100"][1]))
    elif opcao == 2:
        total_pizza += cardapio['pizza']["101"][1]
        lista_carpadio.append(total_pizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Mussarela R$ {:.2f}".format(cardapio['pizza']["102"][1]))
    elif opcao == 3:
        total_pizza += cardapio['pizza']["102"][1]
        lista_carpadio.append(total_pizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Palmito R$ {:.2f}".format(cardapio['pizza']["102"][1]))
    elif opcao == 4:
        total_pizza += cardapio['pizza']["103"][1]
        lista_carpadio.append(total_pizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Frango c/ Caputiry R$ {:.2f}".format(cardapio['pizza']["103"][1]))
    elif opcao == 5:
        sleep(0.5)
        print("\033[32mSaindo do cardápio de Pizza\33[m")
        menu()
    else:
        sleep(0.5)
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")


def carpadio_bebidas():
    total_bebida = 0
    titulo("CARDÁDIO DE BEBIDAS".center(50))
    print("1 - Coca-Cola\n2 - Pepsi\n3 - Suco\n4 - Cerveja\n5 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para escolher a Bebida: ")
    if opcao == 1:
        total_bebida += cardapio["bebida"]["110"][1]
        lista_carpadio.append(total_bebida)
        sleep(0.5)
        print("Você escolheu a bebida Coca-Cola R$ {:.2f}".format(cardapio["bebida"]["110"][1]))
    elif opcao == 2:
        total_bebida += cardapio["bebida"]["111"][1]
        lista_carpadio.append(total_bebida)
        sleep(0.5)
        print("Você escolheu a bebida Pepsi R$ {:.2f}".format(cardapio["bebida"]["111"][1]))    
    elif opcao == 3:
        total_bebida += cardapio["bebida"]["112"][1]
        lista_carpadio.append(total_bebida)
        sleep(0.5)
        print("Você escolheu a bebida Suco R$ {:.2f}".format(cardapio["bebida"]["112"][1])) 
    elif opcao == 4:
        total_bebida += cardapio["bebida"]["113"][1]
        lista_carpadio.append(total_bebida)
        sleep(0.5)
        print("Você escolheu a bebida Cerveja R$ {:.2f}".format(cardapio["bebida"]["113"][1])) 
    elif opcao == 5:
        sleep(0.5)
        print("\033[32mSaindo do cardápio de Bebidas\33[m")
        menu()
    else:
        sleep(0.5)
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")


def cardapio_sobremesa():
    total_sobremesa = 0
    titulo("CARDÁPIO DE SOBREMSA".center(50))
    print("1 - Pudim\n2 - Bolo\n3 - Banana Split\n4 - Gelatina\n5 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para escolher a Sobremesa: ")
    if opcao == 1:
        total_sobremesa += cardapio["sobremesa"]["120"][1]
        lista_carpadio.append(total_sobremesa)
        sleep(0.5)
        print("Você escolhei a sobremesa Pudim R$ {:.2f}".format(cardapio['sobremesa']["120"][1]))
    elif opcao == 2:
        total_sobremesa += cardapio["sobremesa"]["121"][1]
        lista_carpadio.append(total_sobremesa)
        sleep(0.5)
        print("Você escolhei a sobremesa Bolo R$ {:.2f}".format(cardapio['sobremesa']["121"][1]))
    elif opcao == 3:
        total_sobremesa += cardapio["sobremesa"]["122"][1]
        lista_carpadio.append(total_sobremesa)
        sleep(0.5)
        print("Você escolhei a sobremesa Banana Split R$ {:.2f}".format(cardapio['sobremesa']["122"][1]))
    elif opcao == 4:
        total_sobremesa += cardapio["sobremesa"]["123"][1]
        lista_carpadio.append(total_sobremesa)
        print("Você escolhei a sobremesa Gelatina R$ {:.2f}".format(cardapio['sobremesa']["123"][1]))
    elif opcao == 5:
        sleep(0.5)
        print("\033[32mSaindo do cardápio de Sobremesa\33[m")
        menu()
    else:
        sleep(0.5)
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")


def fechar_pedido():
    os.system("cls")
    titulo("FECHAR PEDIDO".center(50))
    print("Seu pedido: ")
    for pedido in lista_carpadio:
        sleep(0.5)
        print(f"R$ {pedido:.2f}")
    total = sum(lista_carpadio)
    print("\033[1;94m-\033[0;0m" *50)
    sleep(0.5)
    print(f"R$ {total:.2f}")
    print("\033[1;94m-\033[0;0m" *50)
    os.system("pause")


def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA DE PIZZARIA ONLINE".center(50))
        print("1 - Cardapio Completo\n2 - Fazer Pedido\n3 - Fechar Pedido\n4 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            carpadio_completo()
        elif opcao == 2:
            os.system("cls")
            carpazio_pizza()
            resposta()
            carpadio_bebidas()
            resposta()
            cardapio_sobremesa()
        elif opcao == 3:
            fechar_pedido()
        elif opcao == 4:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")

menu()
