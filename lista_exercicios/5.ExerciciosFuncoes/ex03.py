"""
03. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 
"""

def soma(n1, n2, n3):
    return(n1 + n2 + n3)


# Programa principal
n1 = int(input("Primeiro número: "))
n2 = int(input("Primeiro número: "))
n3 = int(input("Primeiro número: "))
resultado = n1 + n2 + n3
print(f"{n1} + {n2} + {n3} = {resultado}")
soma(n1, n2, n3)