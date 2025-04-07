"""
06. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""
notas_alunos = []
lista_notas = []
media = 0    

for c in range(10):
    print(f"Aluno: " + str(c+1))
    for j in range(4):
        notas_alunos.append(float(input(f"Notas: " + {j+1} + '\n')))
        media += notas_alunos[j]
        print(f"Média: {media:.1f}")
    media = media / 4
    lista_notas.append(media)

print(lista_notas)
