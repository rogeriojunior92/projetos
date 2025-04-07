"""
07. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
lista_numero = []
soma = 0
multiplicacao = 1

for c in range(0, 5):
    num = int(input(f"Digite o {c+1}º valor: "))
    soma += num
    multiplicacao *= num
    lista_numero.append(num)

print(f"Lista Completa: {lista_numero}")
print(f"Somatória: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")