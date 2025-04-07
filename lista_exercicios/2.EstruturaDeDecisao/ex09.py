"""
09. Faça um Programa que leia três números e mostre-os em ordem decrescente. 
"""
lista = []

lista.append(int(input("Digite o primeiro número: ")))
lista.append(int(input("Digite o segundo número: ")))
lista.append(int(input("Digite o terceiro número: ")))

print(sorted(lista))

