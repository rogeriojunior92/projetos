"""
33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior 
temperaturas informadas, bem como a média das temperaturas. 
"""
soma = media = 0
menor = maior = 0

while True:
    temperatura = float(input("Digite a temperatura (0 para SAIR): "))
    if temperatura == 0:
        break
    soma += temperatura
    media = soma / temperatura

    if temperatura < menor:
        menor = temperatura
    elif temperatura > maior:
        maior = temperatura

print("-" *30)
print(f"Menor temperatura: {menor}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Média da temperatura: {media:.2f}°C")