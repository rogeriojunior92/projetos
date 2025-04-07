"""
08. Faça um programa que leia 5 números e informe a soma e a média dos números. 
"""

soma = 0

for c in range(1, 6):
    num = int(input("Digite o número: "))
    soma += num
 
print(f"Soma é {soma}")
print(f"Média é {soma/5}")
