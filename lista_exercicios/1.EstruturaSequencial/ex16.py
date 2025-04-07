"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a 
serem compradas e o preço total. 
"""

# Tamanho em metros quadrados da área a ser pintada
metros = int(input("Digite o tamanho em metros quadrados da área a ser pintada? "))

# Cobertura da tinta é de 1 litro para cada 3 metros quadrados
litros = metros / 3
# Lata de 18 litros
capacidade_litros = 18
# Preço de R$ 80,00
preco_litros = 80.00
# Quantidade de latas
latas = litros / capacidade_litros
# Total gasto
total = latas * preco_litros

print(f"Você usará {latas:.1f} latas de tinta para pintar.")
print(f"Total de R$ {total:.2f}")