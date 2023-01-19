"""
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram 
para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    a) salários até R$ 280,00 (incluindo) : aumento de 20%
    b) salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    c) salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    d) salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        1) o salário antes do reajuste;
        2) o percentual de aumento aplicado;
        3) o valor do aumento;
        4) o novo salário, após o aumento. 
"""
hora_trabalhada = int(input("Digite o quanto você por hora trabalhada: "))
horas_trabalhadas_mes = int(input("Digite quantas horas você trabalhou no mês: "))
salario_bruto = hora_trabalhada * horas_trabalhadas_mes

if salario_bruto <= 280:
    novo_salario = salario_bruto * 20/100
    print(f"Salário antes do reajuste R$ {salario_bruto}")
    print("Percentual de aumento de 20%")
    print(f"Novo salário é R$ {novo_salario:.2f}")
elif salario_bruto >= 280 and salario_bruto <= 700:
    novo_salario = salario_bruto + (salario_bruto * 15/100)
    print(f"Salário antes do reajuste R$ {salario_bruto}")
    print("Percentual de aumento de 15%")
    print(f"Novo salário é R$ {novo_salario:.2f}")
elif salario_bruto >= 700 and salario_bruto <= 1500:
    novo_salario = salario_bruto + (salario_bruto * 10/100)
    print(f"Salário antes do reajuste R$ {salario_bruto}")
    print("Percentual de aumento de 10%")
    print(f"Novo salário é R$ {novo_salario:.2f}")
elif salario_bruto > 1500:
    novo_salario = salario_bruto + (salario_bruto * 5/100)
    print(f"Salário antes do reajuste R$ {salario_bruto}")
    print("Percentual de aumento de 5%")
    print(f"Novo salário é {novo_salario:.2f}")