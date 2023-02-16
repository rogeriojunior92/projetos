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
import os

while True:
    print("LOJAS TABAJARA")
    print("-" *30)
    total = c = 0

    while True:
        preco = float(input(f"Produto {c+1}: R$ "))
        c +=1
        total += preco
        if preco == 0:
            break     
        
    print("-" *30)
    print(f"Total: R$ {total:.2f}")
    dinheiro = float(input("Dinheiro: R$ "))
    print("-" *30)
    print(f"Troco R$ {dinheiro - total:.2f}")

    print("-" *30)
    print("0 - Reset\n1 - Encerrar")

    opcao = int(input("Qual é a sua opção: "))
    if opcao == 0:
        os.system("cls")
    else:
        print("Saindo do Programa")
        break
