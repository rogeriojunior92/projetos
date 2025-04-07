"""
19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 
"""
lista_numero = []
soma = 0

while True:
    num = int(input("Digite o número: "))

    while num > 1000 or num < 0:
        num = int(input("ERRO! Digite o número entre 0 e 1000: "))
        lista_numero.append(num)
        soma += num

    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        break

print(f"Lista completa: {lista_numero}")
print(f"Menor número da lista {min(lista_numero)}")
print(f"Maior número da lista {max(lista_numero)}")
print(f"Somatória {soma}")