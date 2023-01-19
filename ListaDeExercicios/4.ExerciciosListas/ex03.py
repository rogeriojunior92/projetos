"""
03. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas = []

for c in range(1, 5):
    nota = float(input(f"Digite a {c}ª nota: "))
    notas.append(nota)

print(f"Notas {notas}")
print(f"Média das notas: {sum(notas) / len(notas)}")