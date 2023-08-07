"""
11. Altere o programa anterior para mostrar no final a soma dos números. 
"""
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = 0

for c in range(num1, num2 -1):
    soma +=c
    print(c, end=' ')

print(f"\nSoma {soma}")