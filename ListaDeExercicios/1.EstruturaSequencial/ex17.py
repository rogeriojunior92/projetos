"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro 
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    a) comprar apenas latas de 18 litros;
    b) comprar apenas galões de 3,6 litros;
    c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
"""

metros = int(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
cobertura = metros / 6

lata_litros = 18
preco_lata = 80
galoes_litro = 3.6
galoes_preco = 25.00

# a) comprar apenas latas de 18 litros;
latas = cobertura / lata_litros
total = latas * preco_lata
print("Somente latas de 18L:")
print(f"Para cobrir o metro quadrado de {metros}m², será necessário {latas:.0f}L que custará R$ {total:.2f}")

# b) comprar apenas galões de 3,6 litros;
qtd_galoes = cobertura / galoes_litro
total_galoes = qtd_galoes * galoes_preco
print("Somente latas de 3,6L:")
print(f"Para cobrir o metro quadrado de {metros}m², será necessário {qtd_galoes:.0f}L que custará R$ {total_galoes:.2f}")

# c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 