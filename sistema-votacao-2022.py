import os
from time import sleep

# Listas para armazenar os votos de acordo com o seu candidato
lista_bolsonaro = []
lista_lula = []
lista_ciro_gomes = []
lista_andre_janones = []
lista_leonardo_pericles = []
lista_nulo = []


# Função para criar linha e texto
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


# Função que lê apenas número inteiro e/ou interrupção do teclado pelo usuário
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(TypeError, ValueError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num


# Função para escolher o candidato e adicionar o voto na lista de acordo com o seu candidato
def selecao_candidatos():
    os.system("cls")
    bolsonaro = lula = ciro_gomes = andre_janones = leonardo_pericles = nulo = 0
    titulo("CANDIDATOS PARA PRESIDÊNCIA".center(50))
    print("1 - Bolsonaro\n2 - Lula\n3 - Ciro Gomes\n4 - André Janones\n5 - Leonardo Péricles\n6 - Nulo\n7 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para votar: ")
    if opcao == 1:
        lista_bolsonaro.append(bolsonaro)
        bolsonaro += 1
        print("Você votou em Jair Bolsonaro (PL)")
    elif opcao == 2:
        lista_lula.append(lula)
        lula +=1
        print("Você votou em Lula (PT)")
    elif opcao == 3:
        lista_ciro_gomes.append(ciro_gomes)
        ciro_gomes +=1
        print("Você votou em Ciro Gomes (PDT)")
    elif opcao == 4:
        lista_andre_janones.append(andre_janones)
        andre_janones +=1
        print("Você votou em André Janones (Avante)")
    elif opcao == 5:
        lista_leonardo_pericles.append(leonardo_pericles)
        leonardo_pericles +=1
        print("Você votou em Leonardo Péricles (Unidade Popular)")
    elif opcao == 6:
        lista_nulo.append(nulo)
        nulo +=1
        print("Você votou em Nulo (Sem partido)")
    elif opcao == 7:
        print("\033[32mSaindo da tela de seleção de candidatos\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 7\33[m")


# Função que mostra o resultado final da votação
def resultado_final():
    os.system("cls")
    titulo("RESULTADO DAS ELEIÇÕES 2022".center(50))
    sleep(1)
    print(f"Jair Bolsonaro (PL): {len(lista_bolsonaro)}")
    sleep(1)
    print(f"Lula (PT): {len(lista_lula)}")
    sleep(1)
    print(f"Ciro Gomes (PDT): {len(lista_ciro_gomes)}")
    sleep(1)
    print(f"André Janones (Avante): {len(lista_andre_janones)}")
    sleep(1)
    print(f"Leonardo Péricles (Unidade Popular): {len(lista_leonardo_pericles)}")
    sleep(1)
    print(f"Nulo: {len(lista_nulo)}")


# Função que executa todo o processo
def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA DE VOTAÇÃO 2022".center(50))
        print("1 - Abrir Seleção de Candidatos\n2 - Resultado Final\n3 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            selecao_candidatos()
        elif opcao == 2:
            resultado_final()
        elif opcao == 3:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 3\33[m")
    os.system("pause")

menu()
