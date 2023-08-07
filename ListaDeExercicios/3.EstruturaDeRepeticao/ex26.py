"""
26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. 
"""
candidatoA = candidatoB = candidatoC = 0
eleitores = int(input("Digite a quantidade de eleitores: "))

print("-" *40)
print("SISTEMA VOTAÇÃO".center(40))
print("-" *40)
print("1 - CandidatoA\n2 - CandidatoB\n3 - CandidatoC")
print("-" *40)
for c in range(eleitores +1):
    voto = int(input("Digite a sua opção: "))

    if voto == 1:
        candidatoA +=1
        print(f"Você votou no Candidato A")
    elif voto == 2:
        candidatoB +=1
        print(f"Você votou no Candidato B")
    elif voto == 3:
        candidatoC +=1
        print(f"Você votou no Candidato C")
    else:
        print("Opção Inválida. Digite entre 1 e 3.")

print("-" *40)
print("RESULTADOS DA ELEIÇÃO".center(40))
print("-" *40)
print(f"Candidato A: {candidatoA}")
print(f"Candidato B: {candidatoB}")
print(f"Candidato C: {candidatoC}")
print("-" *40)