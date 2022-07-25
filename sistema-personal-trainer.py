from datetime import date, datetime
import os
from time import sleep

lista_aluno = []
adicionar_preco = []

lista_preco = ("1x semana", 95.00, "2x semana", 95.00, "3x semana", 90.00,
                "Trismestral", 85.00, "Semestral", 80.00, "Anual (consultar)", 00.00)

menu_tabela_preco = {
    "tabela": {
        "100": ["1x semana", 95.00],
        "101": ["2x semana", 95.00],
        "102": ["3x semana", 90.00],
        "103": ["trismestral", 85.00],
        "104": ["semestral", 80.00],
        "105": ["anual", 00.00],
    }
    
}

preco = totalPreco = 0

data = datetime.now()
data_atual = data.strftime("%d/%m/%Y %H:%M")


def titulo(txt):
    print("\033[1;95m-\033[0;0m" *60)
    print("\033[1;45m"+txt+"\033[1;0m")
    print("\033[1;95m-\033[0;0m" *60)


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


def resposta():
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        print("\033[32mSaindo...\33[m")


def tabela_preco():
    os.system("cls")
    titulo("TABELA DE PREÇOS".center(60))
    for c in range(0, len(lista_preco), 2):
        print(f"{lista_preco[c]:.<30} R$ {lista_preco[c+1]:>6.2f}")


def menu_preco():
    totalPreco = 0
    print("\033[1;95m-\033[0;0m" *60)
    print("[1] 1x semana\n[2] 2x semana\n[3] 3x semana\n[4] Trismestral\n[5] Semestral\n[6] Anual (consultar]\n[7] Sair")
    print("\033[1;95m-\033[0;0m" *60)

    opcao = leiaInt("Digite a sua opção / plano: ")
    if opcao == 1:
        print("Você escolheu o plano 1x semana \033[32mR$ 95.00\33[m")
        print("Mensal \033[32mR$ 380.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["100"][1]
        adicionar_preco.append(totalPreco)
    elif opcao == 2:
        print("Você escolheu o plano 2x semana \033[32mR$ 190.00\33[m")
        print("Mensal \033[32mR$ 760.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["101"][1]
        adicionar_preco.append(totalPreco)
    elif opcao == 3:
        print("Você escolheu o plano 3x semana \033[32mR$ 270.00\33[m")
        print("Mensal \033[32mR$ 1080.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["102"][1]
        adicionar_preco.append(totalPreco)
    elif opcao == 4:
        print("Você escolheu o plano Trimestral \033[32mR$ 00.00\33[m")
        print("Mensal \033[32mR$ 00.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["103"][1]
        adicionar_preco.append(totalPreco)
    elif opcao == 5:
        print("Você escolheu o plano Semestral \033[32mR$ 00.00\33[m")
        print("Mensal \033[32mR$ 00.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["104"][1]
        adicionar_preco.append(totalPreco)
    elif opcao == 6:
        print("Você escolheu o plano Anual (consultar) \033[32mR$ 00.00\33[m")
        print("Mensal \033[32mR$ 00.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["105"][1]
        adicionar_preco.append(totalPreco)
    else:
        print("\033[32mSaindo da tabela de preços\33[m")


def cadastrar_aluno():
    titulo("CADASTRO DE ALUNO(A)".center(60))
    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")

    lista_aluno.append((nome, idade, cpf, data_atual))
    sleep(0.5)
    print("\033[32mAluno(a) cadastro com sucesso\33[m")


def listar_aluno():
    titulo("LISTA DE ALUNO(A) CADASTRADO".center(60))
    print("ID".center(3), end='')
    print("Nome".center(20), end='')
    print("Idade".center(20), end='')
    print("CPF".center(20))
    
    for indice_aluno in list(enumerate(lista_aluno, start=1)):

        indice = indice_aluno[0]
        aluno = indice_aluno[1]

        print(str(indice).center(3), end='')
        print(str(aluno[0]).center(20), end='')
        print(str(aluno[1]).center(20), end='')
        print(str(aluno[2]).center(20))

    print("\033[1;95m-\033[0;0m" *60)
    os.system("pause")


def buscar_aluno():
    os.system("cls")
    termo = input("Informe o CPF do aluno(a) para buscar: ")
    print("\033[1;95m-\033[0;0m" *60)
    for cadastro_aluno in lista_aluno:
        nome, idade, cpf, data_atual = cadastro_aluno
        if cpf == termo:
            print(f"Nome: {nome}\nIdade: {idade}\nCPF: {cpf}\nRegistro: {data_atual}")
    print("\033[1;95m-\033[0;0m" *60)
    os.system("pause")


def deletar_aluno():
    os.system("cls")
    termo = input("Informe o CPF do aluno(a) que deseja remover: ")
    print("\033[1;95m-\033[0;0m" *60)
    for cadastro_aluno in lista_aluno:
        nome, idade, cpf, data_atual = cadastro_aluno
        if cpf == termo:
            lista_aluno.remove((nome, idade, cpf, data_atual))
            print(f"CPF {cpf} removido\nData/hora: {data_atual}")
    print("\033[1;95m-\033[0;0m" *60)
    os.system("pause")


def fechar_plano():
    cadastrar_aluno()
    titulo("FECHAR PLANO".center(60))
    valor_total = sum(adicionar_preco)
    print(f"Registro: {data_atual}")
    sleep(0.5)
    print(f"Valor total \033[32mR$ {valor_total:.2f}\33[m")
    print("\033[1;95m-\033[0;0m" *60)


def menu():
    os.system("cls")
    while True:
        titulo("PERSONAL TRAINER BEATRIZ".center(60))
        print("\033[1;97m1 - Listar Aluno\n2 - Buscar Aluno\n3 - Deletar Aluno\n4 - Fechar Plano\n5 - Sair\033[0;0m")
        print("\033[1;95m-\033[0;0m" *60)
        print(f"Ao todo foram cadastrado(s) \033[32m{len(lista_aluno)}\33[m aluno(as)")
        print("\033[1;95m-\033[0;0m" *60)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            listar_aluno()
        elif opcao == 2:
            buscar_aluno()
        elif opcao == 3:
            deletar_aluno()
        elif opcao == 4:
            tabela_preco()
            menu_preco()
            fechar_plano()
            resposta()
        elif opcao == 5:
            print("\033[32mSaindo do programa... Agradeço pela preferência\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 5\33[m")
    os.system("pause")


menu()
