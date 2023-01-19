"""
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e 
mostre o total do seu salário no referido mês. 
"""
ganho_por_hora = int(input("Digite o quanto você ganha por hora: "))
horas_trabalhadas_mes = int(input("Digite a quantidade de horas trabalhadas / mês: "))
salario = ganho_por_hora * horas_trabalhadas_mes

print(f"Ganho por hora: {ganho_por_hora}")
print(f"Horas trabalhadas no mês: {horas_trabalhadas_mes}")
print(f"Salário R$ {salario:.2f}")