"""
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
    
    Exemplo:
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""

valor_hora = int(input("Quanto você ganha por hora trabalhada? R$ "))
horas_trabalhadas_mes = int(input("Quantas horas você trabalhou / mês? R$ "))
salario_bruto = valor_hora * horas_trabalhadas_mes

if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto <= 2500:
    desconto_ir = 0.10
elif salario_bruto > 2500:
    desconto_ir = 0.20

ir = salario_bruto * (5 / 100)
inss = salario_bruto * (10 / 100)
fgts = salario_bruto * (11 / 100)
total_desconto = ir + inss + fgts
salario_liquido = salario_bruto - total_desconto

print("-" *50)
print("SISTEMA FOLHA DE PAGAMENTO".center(50))
print("-" *50)
print(
    f"\nSalário Bruto        : R$ {salario_bruto:.2f}",
    f"\n(-) IR (5%)          : R$ {ir:.2f}",
    f"\n(-) INSS ( 10%)      : R$ {inss:.2f}",
    f"\nFGTS (11%)           : R$ {fgts:.2f}",
    f"\nTotal de descontos   : R$ {total_desconto:.2f}",
    f"\nSalário Liquido      : R$ {salario_liquido:.2f}",
)
print("-" *50)