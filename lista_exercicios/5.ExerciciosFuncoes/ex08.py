"""
08. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 
"""

def digitos(x):
    return len(str(x))

x = int(input("Digite os número: "))
print(f"Total de {digitos(x)} digitos")