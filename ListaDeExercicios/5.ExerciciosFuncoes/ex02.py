"""
02. Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha. 
"""

def cascate02(num):
    for c in range(1, num+1):
        print(c, end=' ')

num = int(input("Entre com o número: "))
cascate02(num)