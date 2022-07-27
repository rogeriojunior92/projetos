import os
from datetime import datetime
from time import sleep

lista_carpadio = []

menu_completo = ("Calabresa", 25.00, "Mussarela", 22.00, "Portguesa", 28.00, "Atum", 30.00, "Bacon", 26.00,
                "Coca-Cola", 9.00, "Pepsi", 8.00, "Guaraná", 7.00, "Água Mineral", 4.50, "Suco", 5.00, "Energetico", 7.00, "Caipirinha", 12.00, "Cerveja", 6.50,
                 "Pudim", 10.00, "Petit Gateau", 18.00, "Açaí", 12.00, "Romeu e Julieta", 15.00, "Chocolate com Nozes", 9.00, "Banana Split", 13.00)


carpadio = {
    "Pizza": {
        "100": ["Calabresa", 25.00],
        "101": ["Mussarela", 22.00],
        "102": ["Portguesa", 28.00],
        "103": ["Atum", 30.00],
        "104": ["Bacon", 26.00],
    },

    "Bebida": {
        "110": ["Coca-Cola", 9.00],
        "111": ["Pepsi", 8.00],
        "112": ["Guaraná", 7.00],
        "113": ["Água Mineral", 4.50],
        "114": ["Suco", 5.00],
        "115": ["Energetico", 7.00],
        "116": ["Caipirinha", 12.00],
        "117": ["Cerveja", 6.50],
    },

    "Sobremesa": {
        "120": ["Pudim", 10.00],
        "121": ["Petit Gateau", 18.00],
        "122": ["Açaí", 12.00],
        "123": ["Romeu e Julieta", 15.00],
        "124": ["Chocolate com Nozes", 9.00],
        "125": ["Banana Split", 13.00],
    }
}


# Função para criar linha e texto
def titulo(txt):
    print("\033[1;96m-\033[0;0m" *50)
    print("\033[1;46m"+txt+"\033[1;0m")
    print("\033[1;96m-\033[0;0m" *50)


def resposta():
    while True:
        resp = input("Quer algo mais? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        print("\033[32mSaindo do menu pizza, bebida e sobremesa\33[m")


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


def cardapio_completo():
    os.system("cls")
    titulo("CARDÁPIO COMPLETO".center(50))
    for c in range(0, len(menu_completo), 2):
        print(f"{menu_completo[c]:.<40} R$ {menu_completo[c+1]:>6.2f}")


def menu_pizza():
    os.system("cls")
    totalPizza = 0
    cardapio_completo()
    titulo("CARDÁPIO DE PIZZA".center(50))
    print("1 - Calabresa\n2 - Mussarela\n3 - Portguesa\n4 - Atum\n5 - Bacon\n6 - Sair")
    print("\033[1;96m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para escolher a Pizza: ")
    if opcao == 1:
        totalPizza += carpadio["Pizza"]["100"][1]
        lista_carpadio.append(totalPizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Calabresa R$ 25,00. Deseja escolher alguma bebida?")
    elif opcao == 2:
        totalPizza += carpadio["Pizza"]["101"][1]
        lista_carpadio.append(totalPizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Mussarela R$ 22,00. Deseja escolher alguma bebida? ")
    elif opcao == 3:
        totalPizza += carpadio["Pizza"]["102"][1]
        lista_carpadio.append(totalPizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Portguesa R$ 28,00. Deseja escolher alguma bebida? ")
    elif opcao == 4:
        totalPizza += carpadio["Pizza"]["103"][1]
        lista_carpadio.append(totalPizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Atum R$ 30,00. Deseja escolher alguma bebida? ")
    elif opcao == 5:
        totalPizza += carpadio["Pizza"]["104"][1]
        lista_carpadio.append(totalPizza)
        sleep(0.5)
        print("Você escolheu a Pizza de Bacon R$ 26,00. Deseja escolher alguma bebida? ")
    elif opcao == 6:
        sleep(0.5)
        print("\033[32mSaindo do cardápio de Pizza\33[m")
        menu()
    else:
        sleep(0.5)
        print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")


def menu_bebida():
    os.system("cls")
    totalBebida = 0
    cardapio_completo()
    titulo("CARDÁPIO DE BEBIDAS".center(50))
    print("1 - Coca-Cola\n2 - Pepsi\n3 - Guaraná\n4 - Água Mineral\n5 - Suco\n6 - Energetico\n7 - Caipirinha\n8 - Cerveja\n9 - Sair")
    print("\033[1;96m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para escolher a Bebida: ")
    if opcao == 1:
        totalBebida += carpadio["Bebida"]["110"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Coca-Cola R$ 9,00. Deseja escolher alguma sobremesa? ")
    elif opcao == 2:
        totalBebida += carpadio["Bebida"]["111"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Pepsi R$ 8,00. Deseja escolher alguma sobremesa? ")
    elif opcao == 3:
        totalBebida += carpadio["Bebida"]["112"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Guaraná R$ 7,00. Deseja escolher alguma sobremesa? ")
    elif opcao == 4:
        totalBebida += carpadio["Bebida"]["113"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Água Mineral R$ 4,50. Deseja escolher alguma sobremesa? ")
    elif opcao == 5:
        totalBebida += carpadio["Bebida"]["114"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Suco R$ 5,00. Deseja escolher alguma sobremesa? ")
    elif opcao == 6:
        totalBebida += carpadio["Bebida"]["115"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Energetico R$ 7,00. Deseja escolher alguma sobremesa? ")
    elif opcao == 7:
        totalBebida += carpadio["Bebida"]["116"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Caipirinha R$ 12,00. Deseja escolher alguma sobremesa? ")
    elif opcao == 8:
        totalBebida += carpadio["Bebida"]["117"][1]
        lista_carpadio.append(totalBebida)
        sleep(0.5)
        print("Você escolheu a bebida Cerveja R$ 6,50. Deseja escolher alguma sobremesa? ")
    elif opcao == 9:
        sleep(0.5)
        print("\033[32mSaindo do cardápio de Bebidas\33[m")
        menu()
    else:
        sleep(0.5)
        print("\033[31mOpção inválida. Digite entre 1 e 9\33[m")


def menu_sobremesa():
    os.system("cls")
    totalSobremesa = 0
    cardapio_completo()
    titulo("CARDÁPIO DE SOBREMESA".center(50))
    print("1 - Pudim\n2 - Petit Gateau\n3 - Açaí\n4 - Romeu e Julieta\n5 - Chocolate com Nozes\n6 - Banana Split\n7 - Sair")
    print("\033[1;96m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para escolher a Sobrenesa: ")
    if opcao == 1:
        totalSobremesa += carpadio["Sobremesa"]["120"][1]
        lista_carpadio.append(totalSobremesa)
        sleep(0.5)
        print("Você escolheu a sobremesa Pudim R$ 10,00. Deseja escolher algo mais? ")
    elif opcao == 2:
        totalSobremesa += carpadio["Sobremesa"]["121"][1]
        lista_carpadio.append(totalSobremesa)
        sleep(0.5)
        print("Você escolheu a sobremesa Petit Gateau R$ 18,00. Deseja escolher algo mais? ")
    elif opcao == 3:
        totalSobremesa += carpadio["Sobremesa"]["122"][1]
        lista_carpadio.append(totalSobremesa)
        sleep(0.5)
        print("Você escolheu a sobremesa Açaí R$ 12,00. Deseja escolher algo mais? ")
    elif opcao == 4:
        totalSobremesa += carpadio["Sobremesa"]["123"][1]
        lista_carpadio.append(totalSobremesa)
        sleep(0.5)
        print("Você escolheu a sobremesa Romeu e Julieta R$ 15,00. Deseja escolher algo mais? ")
    elif opcao == 5:
        totalSobremesa += carpadio["Sobremesa"]["124"][1]
        lista_carpadio.append(totalSobremesa)
        sleep(0.5)
        print("Você escolheu a sobremesa Chocolate com Nozes R$ 9,00. Deseja escolher algo mais? ")
    elif opcao == 6:
        totalSobremesa += carpadio["Sobremesa"]["125"][1]
        lista_carpadio.append(totalSobremesa)
        sleep(0.5)
        print("Você escolheu a sobremesa Banana Split R$ 13,00. Deseja escolher algo mais? ")
    elif opcao == 7:
        sleep(0.5)
        print("\033[32mSaindo do cardápio de Sobremesa\33[m")
    else:
        sleep(0.5)
        print("\033[31mOpção inválida. Digite entre 1 e 7\33[m")


def fechar_pedido():
    os.system("cls")
    titulo("FECHAR O PEDIDO".center(50))  
    data = datetime.now()
    data_atual = data.strftime("%d/%m/%Y %H:%M")
    sleep(0.5)
    print(f"Horário do Pedido {data_atual}")
    for lista in lista_carpadio:
        print(f"R$ {lista:.2f}")
    total = sum(lista_carpadio)
    sleep(0.5)
    print("\033[1;96m-\033[0;0m" *50)
    print(f"Valor R$ {total:.2f}")
    print("\033[1;96m-\033[0;0m" *50)
    os.system("pause")


def menu():
    os.system("cls")
    titulo("SISTEMA DE PIZZARIA".center(50))
    print("1 - Abrir Cardápio de Pizza\n2 - Abrir Cardápio de Bebidas\n3 - Abrir Cardápio de Sobremesa\n4 - Fazer Pedido\n5 - Fechar o Pedido\n6 - Sair")
    print("\033[1;96m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção: ")
    if opcao == 1:
        menu_pizza()
    elif opcao == 2:
        menu_bebida()
    elif opcao == 3:
        menu_sobremesa()
    elif opcao == 4:
        menu_pizza()
        resposta()
        menu_bebida()
        resposta()
        menu_sobremesa()
        menu()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("\033[32mSaindo do programa... Agradecemos pela preferência\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")
    

menu()
