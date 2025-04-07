"""
14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade 
de números impares. 
"""

par = impar = 0

for c in range(1, 11):
    num = int(input(f"Digite o {c+1}º número: "))
    if num % 2 == 0:
        par +=1
    elif num % 2 == 1:
        impar += 1

print(par)
print(impar)