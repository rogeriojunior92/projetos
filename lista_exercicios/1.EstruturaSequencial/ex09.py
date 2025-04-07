"""
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
Formula: C = 5 * ((F-32) / 9).
"""

temperatura = float(input("Digite a temperatura em Fahrenheit: "))
gc = 5 * ((temperatura-32) / 9)

print(f"Temperatura em graus Celsius: {gc:.2f}º")