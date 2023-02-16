"""
43. O cardápio de uma lanchonete é o seguinte:

    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
    Considere que o cliente deve informar quando o pedido deve ser encerrado. 

"""

lista_preco = [["Cachorro Quente", 1.20], ["Bauru Quente", 1.30], ["Bauru com ovo", 1.50], ["Hambúrguer", 1.20],
               ["Cheeseburguer", 1.30], ["Refrigerante ", 1.00]]

lista_final = []

while True:
    print("-" *40)
    print("LANCHONETE TABAJARA".center(40))
    print("-" *40)
    print(
        "Especificação     Código   Preço"
        "\nCachorro Quente   100     R$ 1,20"
        "\nBauru Simples     101     R$ 1,30"
        "\nBauru com ovo     102     R$ 1,50"
        "\nHambúrguer        103     R$ 1,20"
        "\nCheeseburguer     104     R$ 1,30"
        "\nRefrigerante      105     R$ 1,00"
        )
    print("-" *40)
    print("999 para fechar o pedido")
    print("-" *40)

    opcao = int(input("Digite o código do cardápio: "))
    if opcao == 100:
        print("Você escolheu Cachorro Quente")
        qtde = int(input("Quantos lanches? "))
        preco = lista_preco[0][1] * qtde
        lista_final.append(preco)
        print(f"Total de R$ {preco:.2f}")
        
    elif opcao == 101:
        print("Você escolheu Bauru Simples")
        qtde = int(input("Quantos lanches? "))
        preco = lista_preco[1][1] * qtde
        lista_final.append(preco)
        print(f"Total de R$ {preco:.2f}")

    elif opcao == 102:
        print("Você escolheu Bauru com ovo")
        qtde = int(input("Quantos lanches? "))
        preco = lista_preco[2][1] * qtde
        lista_final.append(preco)
        print(f"Total de R$ {preco:.2f}")

    elif opcao == 103:
        print("Você escolheu Hambúrguer")
        qtde = int(input("Quantos lanches? "))
        preco = lista_preco[3][1] * qtde
        lista_final.append(preco)
        print(f"R$ {preco:.2f}")

    elif opcao == 104:
        print("Você escolheu Cheeseburguer")
        qtde = int(input("Quantos lanches? "))
        preco = lista_preco[4][1] * qtde
        lista_final.append(preco)
        print(f"Total de R$ {preco:.2f}")

    elif opcao == 105:
        print("Você escolheu Refrigerante")
        qtde = int(input("Quantas bebidas? "))
        preco = lista_preco[5][1] * qtde
        lista_final.append(preco)
        print(f"Total de R$ {preco:.2f}")

    elif opcao == 999:
        print("-" *40)
        print("FECHAMENTO DA CONTA".center(40))
        print("-" *40)
        print(f"Total de R$ {sum(lista_final):.2f}")
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção Inválida! Tente novamente.")