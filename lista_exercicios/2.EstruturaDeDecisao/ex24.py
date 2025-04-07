"""
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase 
que diga se o número é:

    a) par ou ímpar;
    b) positivo ou negativo;
    c) inteiro ou decimal. 
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while True:
    print("-" *40)
    print("TIPO DE OPERAÇÕES".center(40))
    print("-" *40)
    print("1 - PAR ou IMPAR\n2 - POSITIVO ou NEGATIVO\n3 - INTEIRO ou DECIMAL\n0 - SAIR")
    print("-" *40)

    opcao = int(input("Digite a sua opção: "))
    if opcao == 1:
        if num1 and num2 % 2 == 0:
            print("PAR")
        else:
            print("IMPAR")

    elif opcao == 2:
        if num1 and num2 < 0:
            print("NEGATIVO")
        else:
            print("POSITIVO")

    elif opcao == 3:
        if num1 == num2:
            print("INTEIRO")
        else:
            print("DECIMAL")
        
    elif opcao == 0:
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção Inválida. Digite entre 0 e 3")