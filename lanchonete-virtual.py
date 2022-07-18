import os
from time import sleep

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


def titulo(txt):
    print("\033[36m-\033[0;0m" *40)
    print("\033[36m"+txt+"\033[0;0m")
    print("\033[36m-\033[0;0m" *40)


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


def resposta():
    while True:
        resp = input("Deseja continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        print("Saindo do sub menu itens e/ou bebidas.")


def sub_menu_itens():
    os.system("cls")
    titulo("ESCOLHA O SEU ITEM EXTRA".center(40))
    print("1 - Salada\n2 - Ovo\n3 - Hamburguer\n4 - Salsicha\n5 - Sair")
    print("\033[36m-\033[0;0m" *40)

    opcao = leiaInt("Digite a sua opção: ")
    if opcao == 1:
        print(f"Você adicionou Salada R$ {cardapio['Adicional']['110'][1]} no seu lanche. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 2:
        print(f"Você adicionou Ovo R$ {cardapio['Adicional']['111'][1]} no seu lanche. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 3:
        print(f"Você adicionou Hamburguer R$ {cardapio['Adicional']['112'][1]} no seu lanche. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 4:
        print(f"Você adicionou Salsicha R$ {cardapio['Adicional']['113'][1]} no seu lanche. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 5:
        menu()
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")


def sub_menu_bebida():
    os.system("cls")
    titulo("ESCOLHA A SUA BEBIDA".center(40))
    print("1 - Coca-Cola\n2 - Guaraná\n3 - Pepsi\n4 - Suco\n5 - Sair")
    print("\033[36m-\033[0;0m" *40)

    opcao = leiaInt("Digite a sua opção: ")
    if opcao == 1:
        print(f"Você adicionou Coca-Cola R$ {cardapio['Bebida']['120'][1]}. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 2:
        print(f"Você adicionou Guaraná R$ {cardapio['Bebida']['121'][1]}. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 3:
        print(f"Você adicionou Pepsi R$ {cardapio['Bebida']['122'][1]}. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 4:
        print(f"Você adicionou Suco R$ {cardapio['Bebida']['123'][1]}. Deseja algo mais?")
        sleep(0.5)
    elif opcao == 5:
        menu()
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")

    
def menu():
    os.system("cls")
    while True:
        titulo("LANCHONETE VIRTUAL PYTHON".center(40))
        print("1 - X-Salada\n2 - X-Egg\n3 - X-Burguer\n4 - Hot-dog\n5 - Sair")
        print("\033[36m-\033[0;0m" *40)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            print(f"Você escolheu X-Salada R$ {cardapio['Lanches']['100'][1]}. Deseja adicionar algum item extra? ")
            resposta()
            sub_menu_itens()
            resposta()
            sub_menu_bebida()
            resposta()
        elif opcao == 2:
            print("Você escolheu X-Egg. Deseja adicionar algum item extra? ")
            resposta()
            sub_menu_itens()
            resposta()
            sub_menu_bebida()
            resposta()         
        elif opcao == 3:
            print("Você escolheu X-Burguer. Deseja adicionar algum item extra? ")
            resposta()
            sub_menu_itens()
            resposta()
            sub_menu_bebida()
            resposta()  
        elif opcao == 4:
            print("Você escolheu  Hot-dog. Deseja adicionar algum item extra? ")
            resposta()
            sub_menu_itens()
            resposta()
            sub_menu_bebida()
            resposta()
        elif opcao == 5:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 5!\33[m")
    os.system("pause")

menu()
