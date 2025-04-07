import os

# Variavéis para auxiliar o script
tx_aprovacao = tx_exame = tx_reprovacao = 0
fem_aprovado = fem_exame = fem_reprovado = 0
masc_aprovado = masc_exame = masc_reprovado = 0
c = 0

# Lista para armazenar os dados
lista_princpial = []

# Cadastro de aluno
while True:
    print("-" *40)
    print(f"{c+1}º CADASTRO DE ALUNO".center(40))
    print("-" *40)
    nome = input("Nome do Aluno(a): ")
    while True:
        sexo = input("Sexo: [M/F] ").upper()[0]
        if sexo in "MF":
            break
        print("\033[31mSexo Inválido, digite apenas M ou F.\33[m")
    
    nota1 = float(input(f"Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        print("\033[31mERRO! Digite um número entre 0 e 10.\33[m")
        nota1 = float(input(f"Digite a primeira nota: "))

    nota2 = float(input(f"Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        print("\033[31mERRO! Digite um número entre 0 e 10.\33[m")
        nota2 = float(input(f"Digite a segunda nota: "))
    c+=1

    # Calculo da média das duas notas
    media = (nota1 + nota2) / 2

    if media > 7.0:
        status = 'Aprovado'
    elif media < 7 and media >= 4.0:
        status = 'Exame'
    else:
        status = 'Reprovado'


    # Lista para armazenar os dados coletados
    lista_princpial.append([nome, sexo, [nota1, nota2], media, status])

    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("033[31mERRO! Digite apenas S ou N.\33[m")
    if resp == "N":
        break

# Iteração com a lista principal
for lista in lista_princpial:

    # Se o status for "Aprovado"
    if lista[4] == 'Aprovado':
        tx_aprovacao +=1
        if lista[1] == 'M':
            masc_aprovado +=1
        elif lista[1] == "F":
            fem_aprovado +=1

    elif lista[4] == 'Exame':
        tx_exame +=1
        if lista[1] == 'M':
            masc_exame +=1
        elif lista[1] == "F":
            fem_exame +=1

    elif lista[4] == 'Reprovado':
        tx_reprovacao +=1
        if lista[1] == 'M':
            masc_aprovado +=1
        elif lista[1] == "F":
            fem_reprovado +=1


os.system("cls")
print("\033[34m-\33[m" *40)
print(f"\033[34mLISTA DE TAXA DE STATUS\33[m".center(40))
print("\033[34m-\33[m" *40)
print(f"Aluno(a) Aprovado(s): {tx_aprovacao/len(lista_princpial) *100:.2f}%")
print(f"Aluno(a) Exames: {tx_exame/len(lista_princpial) *100:.2f}%")
print(f"Aluno(a) Reprovado(s): {tx_reprovacao/len(lista_princpial) *100:.2f}%")
print("\033[34m-\33[m" *40)
print(f"\033[34mLISTA DE ALUNOS POR SEXO\33[m".center(40))
print("\033[34m-\33[m" *40)
print(f"Aluna(s) Aprovada(s): {fem_aprovado}")
print(f"Aluna(s) Exame(s): {fem_exame}")
print(f"Aluna(s) Reprovada(s): {fem_reprovado}")
print()
print(f"Aluno(s) Aprovado(s): {masc_aprovado}")
print(f"Aluno(s) Exame(s): {masc_exame}")
print(f"Aluno(s) Reprovado(s): {masc_reprovado}")
print("\033[34m-\33[m" *40)
print(f"Ao todo foram cadastrado(s) \033[32m{len(lista_princpial)}\33[m aluno(s).")
print("\033[34m-\33[m" *40)