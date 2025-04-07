"""
47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve 
fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima 
informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser 
conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

lista_nota = []

nome_atleta = True
while nome_atleta != '':
    nome_atleta = input("Nome [ENTER para encerrar]: ")
    if nome_atleta == "":
        break

    for c in range(0, 7):
        nota = float(input("Nota: "))
        lista_nota.append(nota)

        media = sum(lista_nota) / len(lista_nota)

    print()
    print("Resultado final:")
    print(f"Atleta: {nome_atleta}")
    print(f"Melhor nota: {max(lista_nota):.1f}")
    print(f"Pior nota: {min(lista_nota):.1f}")
    print(f"Média: {media:.1f}")
    print()
    
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        break