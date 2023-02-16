"""
38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
    
    Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
from datetime import datetime

ano = 1995
ano_atual = datetime.now().year
salario_atual = float(input("Digite o salário atual: R$ "))
porcentagem = 1.5/100
salario_final = salario_atual

for c in range(ano, ano_atual +1):
    salario_atual = salario_atual + (porcentagem * salario_final)
    print(f"Ano {c} - R$ {salario_atual:.2f}")
