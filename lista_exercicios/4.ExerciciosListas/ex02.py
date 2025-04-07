"""
02. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista_numero = []

for c in range(1, 11):
    num = float(input(f"Digite o {c}º número: "))
    lista_numero.append(num)

lista_numero.reverse()
print(f"Lista Reversa: {lista_numero:.1f} ")