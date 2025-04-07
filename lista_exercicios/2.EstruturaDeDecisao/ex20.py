"""
20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada 
por aluno e presentar:

    a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    c) A mensagem "Aprovado com Distinção", se a média for igual a 10
"""

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
# a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
if media >= 7:
    print(f"Primeira nota {nota1}")
    print(f"Segunda nota: {nota2}")
    print(f"Terceira nota: {nota3}")
    print(f"Média: {media}")
    print("Status: Aprovado") 

# b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
elif media < 7:
    print(f"Primeira nota {nota1}")
    print(f"Segunda nota: {nota2}")
    print(f"Terceira nota: {nota3}")
    print(f"Média: {media}")
    print("Reprovado")

# c) A mensagem "Aprovado com Distinção", se a média for igual a 10
elif media > 10:
    print(f"Primeira nota {nota1}")
    print(f"Segunda nota: {nota2}")
    print(f"Terceira nota: {nota3}")
    print(f"Média: {media}")
    print("Aprovado com Distinção")