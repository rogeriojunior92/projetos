"""
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido. 
"""
while True:
    print('-' *40)
    print('CALENDÁRIO SEMANAL'.center(40))
    print('-' *40)
    print('1 - Domingo\n2 - Segunda-Feira\n3 - Terça-Feira\n4 - Quarta-Feira\n5 - Quinta-Feira\n6 - Sexta-Feira\n0 - Sair')
    print('-' *40)

    opcao = int(input("Digite a sua opção: "))
    if opcao == 1:
        print('Domingo')
    elif opcao == 2:
        print('Segunda-Feira')
    elif opcao == 3:
        print('Terça-Feira')
    elif opcao == 4:
        print('Quarta-Feira')
    elif opcao == 5:
        print('Quinta-Feira')
    elif opcao == 6:
        print('Sexta-Feira')
    elif opcao == 0:
        print("Saindo do programa")
        break
    else:
        print("Valor Inválida! Digite apenas 0 até 6")

