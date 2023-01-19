"""
03. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
"""
while True:
    print("-" *40)
    print("VALIDAÇÃO DE SEXO".center(40))
    print("-" *40)
    print("[F] Feminino\n[M] Masculino\n[S] Sair")
    print("-" *40)

    opcao = input("Digite a sua opção: ").upper()[0]
    if opcao == "F":
        print("Feminino")
    elif opcao == "M":
        print("Masculino")
    elif opcao == "S":
        print("Saindo da programa!")
        break
    else:
        print("Opção e/ou sexo invalido.")
   