"""
17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será 
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco 
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o 
exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

texto_salto = ["Primeiro Salto", "Segundo Salto", "Terceiro Salto", "Quarto Salto", "Quinto Salto"]
lista_atleta = []
lista_salto = []

while True:
    print("-" *35)
    atleta = input("Atleta (ENTER para encerrar): ")
    if atleta == "":
        break
    lista_atleta.append(atleta)

    print(f"Atleta: {atleta}")

    for c in range(5):
        salto = float(input(f"{texto_salto[c]}: "))
        lista_salto.append(salto)
    
    media = sum(lista_salto) / len(lista_salto)
    print("-" *35)
    print("Resultado final:")
    print(f"Atleta: {atleta}")
    print(f"Saltos: {lista_salto}")
    print(f"Média dos Saltos: {media:.1f}m")
print("-" *35)