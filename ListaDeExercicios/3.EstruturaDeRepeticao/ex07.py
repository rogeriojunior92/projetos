"""
07. Faça um programa que leia 5 números e informe o maior número. 
"""

lista = []
for c in range(1, 6):
    num = int(input(f"Digite o {c+1}º valor: "))
    lista.append(num)

print(f"Maior número digitado é {max(lista)}")