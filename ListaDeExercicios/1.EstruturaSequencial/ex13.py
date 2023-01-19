"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""

while True:
    print("-" *40)
    print("CALCULO PESO IDEAL".center(40))
    print("-" *40)
    print("1 - Homem\n2 - Mulher\n0 - Sair")
    print("-" *40)

    opcao = int(input("Digite a sua opção: "))
    if opcao == 1:
        h = float(input("Altura: "))
        peso = float(input("Peso: "))
        formula = (72.7*h) - 58
        print(f"Peso ideal {formula:.2f}kg")
    
    elif opcao == 2:
        h = float(input("Altura: "))
        peso = float(input("Peso: "))
        formula = (62.1*h) - 44.7
        print(f"Peso ideal {formula:.2f}Kg")

    elif opcao == 0:
        print("Saindo do programa")
        break
    else:
        print("Opção Inválida! Digite entre 0 e 3.")