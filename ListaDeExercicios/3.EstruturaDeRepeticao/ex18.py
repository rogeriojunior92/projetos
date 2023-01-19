"""
18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos 
valores. 
"""

lista_numero = []
soma = 0

while True:
    num = int(input("Digite o número: "))
    lista_numero.append(num)
    soma += num

    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        break

print(f"Lista completa dos números: {lista_numero}")
print(f"Menor valor digitado é {min(lista_numero)}")
print(f"Maior valor digitado é {max(lista_numero)}")
print(f"Somatória é {soma}")