"""
06. Faça um Programa que leia três números e mostre o maior deles. 
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 > num3:
    print(f"Primeiro número: {num1}")
    print(f"Segundo número: {num2}")
    print(f"Primeiro número: {num3}")
    print("Primeiro número é maior")
elif num2 > num1 > num3:
    print(f"Segundo número: {num2}")
    print(f"Primeiro número: {num1}")
    print(f"Terceiro número: {num3}")
    print("Segundo número é maior")
elif num3 > num1 > num2:
    print(f"Terceiro número: {num2}")
    print(f"Primeiro número: {num1}")
    print(f"Segundo número: {num3}")
    print("Terceiro número é maior")