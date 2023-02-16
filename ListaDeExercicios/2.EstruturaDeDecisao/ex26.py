"""
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    a) Álcool:
    b) até 20 litros, desconto de 3% por litro
    c) acima de 20 litros, desconto de 5% por litro
    
    Gasolina:
    a) até 20 litros, desconto de 4% por litro
    b) acima de 20 litros, desconto de 6% por litro. 
    
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: 
    A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
"""

litro_gasolina = 2.50
litro_alcool = 1.90

while True:
    print("-" *40)
    print("POSTO COMBUSTÍVEL PYTHON".center(40))
    print("-" *40)
    print("1) A-álcool\n2) G-gasolina\n0) Sair")
    print("-" *40)

    opcao = int(input("Digite a sua opção: "))
    print("-" *40)
    if opcao == 1:
        litros_vendidos = int(input("Digite a quantidade de litros para Álcool: "))
        if litros_vendidos <= 20:
            total_gasolina = litros_vendidos * litro_gasolina
            desc_gasol = total_gasolina - (total_gasolina * 3/100)
            print(f"Você abasteceu {litros_vendidos} litros")
            print(f"Valor de R$ {total_gasolina:.2f}")
            print(f"Desconto de 3% é R$ {desc_gasol:.2f}")
        elif litros_vendidos > 20:
            total_gasolina = litros_vendidos * litro_gasolina
            desc = total_gasolina - (total_gasolina * 5/100)
            print(f"Você abasteceu {litros_vendidos} litros")
            print(f"Valor de R$ {total_gasolina:.2f}")
            print(f"Desconto de 5% é R$ {desc:.2f}")
            print("-" *40)            

    elif opcao == 2:
        litros_vendidos = int(input("Digite a quantidade de litros para Gasolina: "))
        if litros_vendidos <= 20:
            total_alcool = litros_vendidos * litro_alcool
            desc_alcool = total_alcool - (total_alcool * 4/100)
            print(f"Você abasteceu {litros_vendidos} litros")
            print(f"Valor de R$ {total_alcool:.2f}")
            print(f"Desconto de 4% é R$ {desc_alcool:.2f}")
            print("-" *40) 
        elif litro_alcool > 20:
            total_alcool = litros_vendidos * litro_alcool
            desc_alcool = total_alcool - (total_alcool * 6/100)
            print(f"Você abasteceu {litros_vendidos} litros")
            print(f"Valor de R$ {total_alcool:.2f}")
            print(f"Desconto de 6% é R$ {desc_alcool:.2f}")
            print("-" *40) 
    elif opcao == 3:
        print("Saindo do Programa. Até breve!")
        break
    else:
        print("Opção Inválida. Digite entre 0 e 2")