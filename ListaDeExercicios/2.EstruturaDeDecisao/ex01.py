"""
01. Faça um Programa que peça dois números e imprima o maior deles. 
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("Primeiro número é maior que o segundo número")
elif num2 > num1: 
    print("Segundo número é maior que o primeiro número")
else:
    print("Ambos números são iguais")