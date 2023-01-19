"""
04. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento for "0" zero ou 
negativo. 
"""

def caracteres(x):
    if x > 0:
        print("P - Positivo")
    elif x < 0:
        print("N - Negativo")
    elif x == 0:
        print("igual a zero")

caracteres(int(input("Digite o valor: ")))