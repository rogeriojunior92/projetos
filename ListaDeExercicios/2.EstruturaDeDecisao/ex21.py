"""
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 
"""

print("-" *50)
print("BEM-VINDO AO CAIXA ELETRÔNICO".center(50))
print("-" *50)

saque = float(input("Digite o valor do saque desejado: R$ "))
while saque < 10 or saque > 600:
    print('Valor inválido! Digite um valor maior que R$10 e menor que R$600.')
    saque = float(input("Digite o valor do saque desejado: R$ "))

nota100 = saque // 100
resto100 = nota100 % 100

nota50 = saque // 50
resto50 = nota50 % 50

nota10 = saque // 10
resto10 = nota10 % 10

nota5 = saque // 5
resto5 = saque % 5

nota1 = saque // 1
resto1 = saque % 1

print(f"Total de {nota100:.0f} cédulas de R$ 100,00")
print(f"Total de {nota50:.0f} cédulas de R$ 50,00")
print(f"Total de {nota10:.0f} cédulas de R$ 10,00")
print(f"Total de {nota5:.0f} cédulas de R$ 5,00")
print(f"Total de {nota1:.0f} cédulas de R$ 1,00")