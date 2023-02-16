"""
40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

    a) Código da cidade;
    b) Número de veículos de passeio (em 1999);
    c) Número de acidentes de trânsito com vítimas (em 1999). 
    Deseja-se saber:
    d) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    e) Qual a média de veículos nas cinco cidades juntas;
    f) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. 
"""

maior = menor = media = soma_veiculo = soma_acidente = 0

for c in range(1, 6):
    codigo = int(input("Código da cidade: "))
    veiculo = int(input("Número de veículos de passeio (em 1999): "))
    acidente = int(input("Número de acidentes de trânsito com vítimas (em 1999): "))

    soma_veiculo += veiculo
    soma_acidente += acidente

    if acidente > maior:
        maior = acidente

