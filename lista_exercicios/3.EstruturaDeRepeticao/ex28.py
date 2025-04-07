"""
28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade 
de CDs e o valor para em cada um. 
"""
total = media = 0

cds = int(input("Digite a quantidade de CDs: "))

for c in range(1, cds +1):
    preco = float(input("Preço: R$ "))
    total += preco # Soma
    media = total / cds

print("-" *30)
print(f"O valor total R$ {total:.2f}")
print(f"O valor gasto média por CD é R$ {media:.2f}")