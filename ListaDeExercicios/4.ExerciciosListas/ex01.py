"""
01. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
lista_numero = []

for c in range(1, 6):
    num = int(input(f"Digite o {c}º número: "))
    lista_numero.append(num)

print(lista_numero)