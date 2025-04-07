"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

print("Analisando as notas....")
print(f"Primeira Nota: {nota1}")
print(f"Segunda Nota: {nota2}")
print(f"Terceira Nota: {nota3}")
print(f"Quarta Nota: {nota4}")
print('-------------------------')
print(f"Média {media}")