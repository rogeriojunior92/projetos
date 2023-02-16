"""
44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

    1 , 2, 3, 4  - Votos para os respectivos candidatos 
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

    Faça um programa que calcule e mostre:
    a) O total de votos para cada candidato;
    b) O total de votos nulos;
    c) O total de votos em branco;
    d) A percentagem de votos nulos sobre o total de votos;
    e) A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. 
"""

bolsonaro = lula = ciro = simone = nulo = voto_branco = total = soma = 0

lista_total_votos = []

while True:
    print("-" *40)
    print("VOTAÇÃO TABAJARA 2022".center(40))
    print("-" *40)
    print("1 - Jair Bolsonaro (PL)\n2 - Luiz Inácio Lula da Silva (PT)\n3 - Ciro Gomes (PDT)\n4 - Simone Tebet (MDB)\n5 - Voto Nulo\n6 - Voto em Branco\n0 - Sair")
    print("-" *40)

    opcao = int(input("Digite a opção do seu candidato: "))
    if opcao == 1:
        print("Você votou no Jair Bolsonaro (PL)")
        bolsonaro += 1
        soma +=1

    elif opcao == 2:
        print("Você votou no JLuiz Inácio Lula da Silva (PT)")
        lula +=1
        soma +=1

    elif opcao == 3:
        print("Você votou noCiro Gomes (PDT)")
        ciro +=1
        soma +=1

    elif opcao == 4:
        print("Você votou na Simone Tebet (MDB)")
        simone +=1  
        soma +=1
    elif opcao == 5:
        print("Você votou Nulo")
        nulo +=1
        soma +=1
    elif opcao == 6:
        print("Você votou em Branco")
        voto_branco +=1
        soma +=1

    elif opcao == 0:
        print("Saindo do Votação. Até breve!")
        break
    else:
        print("Opção Inválida. Digite entre 0 e 6")

print("A) O total de votos para cada candidato: ")
print("-" *40)
print(f"Jair Bolsonaro (PL): {bolsonaro}")
print(f"Luiz Inácio Lula da Silva (PT): {lula}")
print(f"Ciro Gomes (PDT): {ciro}")
print(f"Simone Tebet (MDB): {simone}")
print(f"O total de votos nulos: {nulo}")
print(f"O total de votos em branco: {voto_branco}")
print(f"A percentagem de votos nulos sobre o total de votos:")
print(f"Total de Votos: {soma} - Voto em Branco {soma/nulo *100}%")
print("A percentagem de votos em branco sobre o total de votos.")
print("-" *40)