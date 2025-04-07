"""
12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 
13 anos possuem altura inferior à média de altura desses alunos.
"""
from datetime import datetime

lista_altura = []
lista_idade = []
media = 0

for c in range(5):
    print(f"{c+1}º ALUNO")
    ano_nascimento = int(input("Ano de Nascimento: "))
    idade = datetime.now().year - ano_nascimento
    altura = float(input("Altura: "))

    lista_altura.append(altura)
    lista_idade.append(idade)
    media = sum(lista_altura) / len(lista_altura)

print("ANALISANDO OS DADOS")
print(f"Lista de Altura: {lista_altura}")
print(f"Lista de Idade: {lista_idade}")
print(f"Média de Altura: {media:.2f}")
