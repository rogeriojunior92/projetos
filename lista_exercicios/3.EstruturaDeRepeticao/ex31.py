"""
31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora 
rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final 
da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara 
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ...
"""
while True:
    print("-" *40)
    print("LOJAS TABAJARA".center(40))
    print("-" *40)

    c = total = 0
    while True:
        preco_mercadoria = float(input(f"Produto {c+1}: R$ "))
        if preco_mercadoria == 0:
            break
        
        c+=1
        total += preco_mercadoria

    dinheiro = float(input("Digite a quantia para pagar: R$ "))
    troco = dinheiro - total

    print("-" *40)
    print(f"Total: R$ {total:.2f}")
    print(f"Dinheiro: R$ {dinheiro:.2f}")
    print(f"Troco: R$ {troco:.2f}")
    print("-" *40)
    
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("\033[31mERRO! Digite apenas S ou N.")
    if resp == "N":
        break