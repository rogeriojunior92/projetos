"""
05. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no 
vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
lista = []
lista_par = []
lista_impar = []

for c in range(1, 21):
    num = int(input(f"Digite o {c}º número: "))
    lista.append(num)

    if num % 2 == 0:
        lista_par.append(num)
    elif num % 2 == 1:
        lista_impar.append(num)

print(f"Lista Completa: {lista}")
print(f"Lista Par: {lista_par}")
print(f"Lista Ímpar: {lista_impar}")