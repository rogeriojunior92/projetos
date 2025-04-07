"""
16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos 
seguintes intervalos de valores:

a) $200 - $299
b) $300 - $399
c) $400 - $499
d) $500 - $599
e) $600 - $699
f) $700 - $799
g) $800 - $899
h) $900 - $999
i) $1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""
lista = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699],
         [700, 799], [800, 899], [900, 999], [1000]]

vendedor = input("Nome do Vendedor? ")
vendas = float(input("Quanto vendeu na semana trabalhada? R$ "))
salario = float(input("Salário: R$ "))
comissao = vendas * 9/100
novo_salario = salario + comissao

print("-" *40)
if lista[0]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[1]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[2]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[3]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[4]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[5]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[6]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[7]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[8]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
elif lista[9]:
    print(f"Vendedor: {vendedor}")
    print(f"Total de Vendas R$ {vendas:.2f}")
    print(f"Salário R$ {salario:.2f}")
    print(f"Comissão: {comissao:.2f}")
    print(f"Novo Salário R$ {novo_salario:.2f}")
print("-" *40)