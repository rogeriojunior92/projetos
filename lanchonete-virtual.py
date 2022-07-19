import os
from time import sleep

'''
Lista para armazenar os valores do pedido.
'''
lista_total = []
valor_total = totalLanche = totalItem = totalBebida = 0 

'''
Tupla para imprimir o cardápio completo produto x preço
'''
menu_completo = ("X-Salada", 12.90, "X-Egg", 11.90, "X-Burguer", 10.90, "Hot-dog", 6.50, "Salada (adicional)", 0.50, "Ovo (adicional)", 1.00, "Hamburguer (adicional)", 2.00,
                 "Salsicha (adicional)", 1.50, "Coca-Cola", 5.90, "Guaraná", 4.90, "Pepsi", 4.50, "Suco", 4.00)

'''
Dicionário cardápio, para auxiliar nas variáveis de lanche x preço
'''
cardapio = {
    "Lanches": {
        "100": ["X-Salada", 12.90],
        "101": ["X-Egg", 11.90],
        "102": ["X-Burguer", 10.90],
        "103": ["Hot-dog", 6.50]
    },

    "Adicional": {
        "110": ["Salada", 0.50],
        "111": ["Ovo", 1.00],
        "112": ["Hamburguer", 2.00],
        "113": ["Salsicha", 1.50]
    },

    "Bebida": {
        "120": ["Coca-Cola", 5.90],
        "121": ["Guaraná", 4.90],
        "122": ["Pepsi", 4.50],
        "123": ["Suco", 4.00]
    },
}

'''
Função para criar linha e titulo
'''
def titulo(txt):
    print("\033[36m-\033[0;0m" *40)
    print("\033[36m"+txt+"\033[0;0m")
    print("\033[36m-\033[0;0m" *40)


'''
Função para entrada de número inteiro e interrupção do teclado
'''
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num

'''
Função para validar resposta do usuário
'''
def resposta():
    while True:
        resp = input("Deseja continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        print("\033[32mSaindo do sub menu itens e/ou bebidas.\33[m")


'''
Função para imprimir cardápio
'''
def carpadio_completo():
    os.system("cls")
    titulo("CARDÁPIO PRINCIPAL".center(40))
    for c in range(0, len(menu_completo), 2):
        print(f"{menu_completo[c]:.<30} R$ {menu_completo[c+1]:>6.2f}")

'''
Função para imprimir cardápio lanche
'''
def cardapio_lanches():
    totalLanche = 0
    os.system("cls")
    carpadio_completo()
    titulo("CARDÁPIO DE LANCHES".center(40))
    print("1 - X-Salada\n2 - X-Egg\n3 - X-Burguer\n4 - Hot-dog\n5 - Sair")
    print("\033[36m-\033[0;0m" *40)

    opcao = leiaInt("Digite a sua opção: ")
    if opcao == 1:
        print(f"Você escolheu X-Salada R$ {cardapio['Lanches']['100'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalLanche += cardapio["Lanches"]['100'][1]
        lista_total.append(totalLanche)
    elif opcao == 2:
        print(f"Você escolheu X-Egg R$ {cardapio['Lanches']['101'][1]}\nDeseja adicionar algum item extra e/ou bebida? ")
        totalLanche += cardapio["Lanches"]['101'][1]
        lista_total.append(totalLanche)
    elif opcao == 3:
        print(f"Você escolheu X-Burguer R$ {cardapio['Lanches']['103'][1]}\nDeseja adicionar algum item extra e/ou bebida? ")
        totalLanche += cardapio["Lanches"]['102'][1]
        lista_total.append(totalLanche)
    elif opcao == 4:
        print(f"Você escolheu Hot-dog R$ {cardapio['Lanches']['103'][1]}\nDeseja adicionar algum item extra e/ou bebida? ")
        totalLanche += cardapio["Lanches"]['103'][1]
        lista_total.append(totalLanche)
    elif opcao == 5:
        sleep(0.5)
        print("\033[32mSaindo do Cardápio de Lanches\33[m")
        menu()
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")     


'''
Função para imprimir cardápio adicional extra
'''
def carpadio_itens():
    totalItem = 0
    os.system("cls")
    carpadio_completo()
    titulo("CARDÁPIO DE ADICIONAL".center(40))
    print("1 - Salada\n2 - Ovo\n3 - Hamburguer\n4 - Salsicha\n5 - Sair")
    print("\033[36m-\033[0;0m" *40)

    opcao = leiaInt("Digite a sua opção: ")
    if opcao == 1:
        print(f"Você adicionou Salada R$ {cardapio['Adicional']['110'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalItem += cardapio["Adicional"]['110'][1]
        lista_total.append(totalItem)
    elif opcao == 2:
        print(f"Você adicionou Ovo R$ {cardapio['Adicional']['111'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalItem += cardapio["Adicional"]['111'][1]
        lista_total.append(totalItem)
    elif opcao == 3:
        print(f"Você adicionou Hamburguer R$ {cardapio['Adicional']['112'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalItem += totalItem + cardapio["Adicional"]['112'][1]
        lista_total.append(totalItem)
    elif opcao == 4:
        print(f"Você adicionou Salsicha R$ {cardapio['Adicional']['113'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalItem += totalItem + cardapio["Adicional"]['113'][1]
        lista_total.append(totalItem)
    elif opcao == 5:
        sleep(0.5)
        print("\033[32mSaindo do Cardápio de Item Extra\33[m")
        menu()
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m") 


'''
Função para imprimir cardápio de bebidas
'''
def carpadio_bebida():
    totalBebida = 0
    os.system("cls")
    titulo("CARDÁPIO DE BEBIDAS".center(40))
    print("1 - Coca-Cola\n2 - Guaraná\n3 - Pepsi\n4 - Suco\n5 - Sair")
    print("\033[36m-\033[0;0m" *40)

    opcao = leiaInt("Digite a sua opção: ")
    if opcao == 1:
        print(f"Você escolheu Coca-Cola R$ {cardapio['Bebida']['120'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalBebida += cardapio["Bebida"]['120'][1]
        lista_total.append(totalBebida)
    elif opcao == 2:
        print(f"Você escolheu Guaraná R$ {cardapio['Bebida']['121'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalBebida += cardapio["Bebida"]['121'][1]
        lista_total.append(totalBebida)
    elif opcao == 3:
        print(f"Você escolheu Pepsi R$ {cardapio['Bebida']['122'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalBebida += cardapio["Bebida"]['122'][1]
        lista_total.append(totalBebida)
    elif opcao == 4:
        print(f"Você escolheu Suco R$ {cardapio['Bebida']['123'][1]}\nDeseja adicionar algum item extra e/ou bebida?")
        totalBebida += cardapio["Bebida"]['123'][1]
        lista_total.append(totalBebida)
    elif opcao == 5:
        sleep(0.5)
        print("\033[32mSaindo do Cardápio de Bebidas\33[m")
        menu()
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")


'''
Função para somar o valor total do pedido
'''
def fechar_pedido():
    os.system("cls")
    titulo("FECHANDO O PEDIDO".center(40))
    valor_total = sum(lista_total)
    print(f"Valor do Pedido R$ {valor_total:.2f}")
    print("\033[36m-\033[0;0m" *40)
    os.system("pause")


'''
Função que executa todo o processo
'''
def menu():
    os.system("cls")
    while True:
        titulo("LANCHONETE VIRTUAL PYTHON".center(40))
        print("1 - Carpádio Completo\n2 - Cardápio de Lanches\n3 - Cardápio de Itens Extra\n4 - Cardápio de Bebidas\n5 - Fazer Pedido\n6 - Finalizar Pedido\n7 - Sair")
        print("\033[36m-\033[0;0m" *40)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            carpadio_completo()
        elif opcao == 2:
            cardapio_lanches()
        elif opcao == 3:
            carpadio_itens()
        elif opcao == 4:
            carpadio_bebida()
        elif opcao == 5:
            cardapio_lanches()
            resposta()
            carpadio_itens()
            resposta()
            carpadio_bebida()
        elif opcao == 6:
            fechar_pedido()
        elif opcao == 7:
            sleep(0.5)
            print("\033[32mSaindo do programa... Agradecemos pela preferência!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 7!\33[m")

menu()
