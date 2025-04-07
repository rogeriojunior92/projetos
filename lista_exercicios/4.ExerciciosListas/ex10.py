"""
10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos 
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

lista_A = []
lista_B = []
lista_C = []

for c in range(0, 10):
    num = int(input(f"Digite o {c+1}º valor da Lista A: "))
    lista_A.append(num)

for c in range(0, 10):
    num = int(input(f"Digite o {c+1}º valor da Lista B: "))
    lista_B.append(num)

for c in range(0, 20):
    lista_C.append(lista_A[c])
    lista_C.append(lista_B[c])

print(f"Lista A: {lista_A}")
print(f"Lista B: {lista_B}")
print(f"Lista C: {lista_C}")