"""
09. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos 
elementos do vetor.
"""
lista_A = []
soma = 0
for c in range(0, 10):
    soma_dos_quadrados = int(input(f"Digite o {c+1}º valor: ")) ** 2
    soma += soma_dos_quadrados
    lista_A.append(soma_dos_quadrados)
    
print(f"Lista dos números digitados: {lista_A}")
print(f"A soma dos quadrados dos numeros digitados é {soma}")
