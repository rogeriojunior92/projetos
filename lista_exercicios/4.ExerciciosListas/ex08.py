"""
08. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
from datetime import datetime

lista_altura = []
lista_idade = []

for c in range(0, 5):
    ano_nascimento = int(input("Ano de Nascimento: "))
    idade = datetime.now().year - ano_nascimento
    altura = float(input("Altura: "))
    
    lista_altura.append(altura)
    lista_idade.append(idade)

lista_altura.reverse()
lista_idade.reverse()

print(f"Lista de Altura: {lista_altura}")
print(f"Lista de Idade: {lista_idade}")


    