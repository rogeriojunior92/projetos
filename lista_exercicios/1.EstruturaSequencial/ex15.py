"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    a) salário bruto.
    b) quanto pagou ao INSS.
    c) quanto pagou ao sindicato.
    d) o salário líquido.
    e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
    
Obs.: Salário Bruto - Descontos = Salário Líquido. 
"""

print("Favor, preencher os campos abaixo: ")
ganha_por_hora = int(input("Quanto você ganha por hora? "))
horas_trabalhadas_mes = int(input("Quantas horas você trabalhou no mês? "))
salario_bruto = ganha_por_hora * horas_trabalhadas_mes

ir = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(
    f"\n+ Salário Bruto : R$ {salario_bruto:.2f}",
    f"\n- IR (11%) : R$ {ir:.2f}",
    f"\n- INSS (8%) : R$ {inss:.2f}",
    f"\n- Sindicato ( 5%) : R$ {sindicato:.2f}",
    f"\n= Salário Liquido : R$ {salario_liquido:.2f}"
)