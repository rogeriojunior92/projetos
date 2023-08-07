"""
17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 
"""

from datetime import datetime

ano = int(input("Digite um ano: "))
ano_atual = datetime.now().year
contagem = 0

for c in range(ano, ano_atual +1):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(c)
        contagem +=1
print(f'bissextos: {contagem}')