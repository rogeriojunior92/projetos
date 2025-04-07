"""
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte Fórmula: (72.7*altura) - 58 
"""

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

formula = (72.7*altura) - 58 

print(f"Altura: {altura}")
print(f"Peso: {peso}Kg")
print(f"Peso ideal: {formula}kg")