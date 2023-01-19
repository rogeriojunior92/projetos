"""
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 
"""

while True:
    print("-"*40)
    print("PERIODO DE ESTUDO".center(40))
    print("-"*40)
    print("[M] Matutino\n[V] Vespertino\n[N] Noturno\n[S] Sair")
    print("-"*40)

    opcao = input("Digite a sua opção: ")
    if opcao == "Mf":
        print("Bom Dia!")
    elif opcao == "Vv":
        print("Boa Tarde!")
    elif opcao == "Nn":
        print("Boa Noite!")
    elif opcao == "Ss":
        print("Saindo do programa")
        break
    else:
        print("Opção e/ou valor Inválido!")