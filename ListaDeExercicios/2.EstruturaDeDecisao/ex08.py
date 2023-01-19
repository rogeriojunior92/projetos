"""
08. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato. 
"""
produto1 = float(input("Digite o preço do primeiro produto: R$ "))
produto2 = float(input("Digite o preço do segundo produto: R$ "))
produto3 = float(input("Digite o preço do terceiro produto: R$ "))

if produto1 < produto2 < produto3:
    print(f"O primeiro produto é mais barato, tem o valor de R$ {produto1:.2f}")
elif produto2 < produto1 < produto3:
    print(f"O segundo produto é mais barato, tem o valor de R$ {produto2:.2f}")
elif produto3 < produto1 < produto2:
    print(f"O terceiro produto é mais barato, tem o valor de R$ {produto3:.2f}")