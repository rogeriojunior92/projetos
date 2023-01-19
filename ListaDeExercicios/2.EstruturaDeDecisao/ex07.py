"""
07. Faça um Programa que leia três números e mostre o maior e o menor deles. 
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o terceiro número: "))
num3 = int(input("Digite o quarto número: "))

if num1 > num2 > num3:
    print("Primeiro número é maior")
elif num2 > num1 > num3:
    print("Segundo número é maior")
elif num3 > num1 > num2:
    print("Terceiro número é maior")
else:
    print("Ambos os números são iguais")