"""
27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos. 
"""
media = 0

qtde_turma = int(input("Digite a quantidade de turma: "))
for c in range(qtde_turma +1):
    while True:
        qtde_aluno = int(input(f"Digite quantos alunos tem na turma {c+1}: "))
        if qtde_aluno <= 40:
            break

    media = ((media * c) + qtde_aluno) / (c + 1)

print(f"A media de alunos por turma é {media:.2f}")