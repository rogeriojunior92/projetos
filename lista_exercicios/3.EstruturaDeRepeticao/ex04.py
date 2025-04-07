"""
04. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 
3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que 
calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população 
do país B, mantidas as taxas de crescimento. 
"""

a = 80000
b = 200000
ano = 0

while a <= b:
    a += a * 0.03
    b += b * 1.5
    ano += 1

print(f"Poluação de A: {a}")
print(f"Poluação de B: {b}")
print("O ultrasse ou iguale a população entre A e B em {ano} anos")