"""
22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). 
"""

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"Número digitado {num} é PAR")
elif num % 2 == 1:
    print(f"Número digitado {num} é IMPAR")