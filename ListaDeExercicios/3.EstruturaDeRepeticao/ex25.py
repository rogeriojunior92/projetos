"""
25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 
"""

pessoas = int(input("Quantas pessoas? "))
soma = media = 0

for c in range(1, pessoas +1):
    idade = int(input("Idade: "))
    soma += idade
    media = soma / pessoas
    
    if media <= 25:
        print("Jovem")
    elif media > 26 and media <= 59:
        print("Adulto(a)")
    else:
        print("Idoso(a)")

print("-" *30)
print(f"Soma das Idade: {soma}")
print(f"Média de Idade: {media:.2f}")