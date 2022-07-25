from datetime import date, datetime
import os
from time import sleep

'''
Sistema de controle personal trainer, o objetivo do script:
1. Mostrar a quantidade de treino x preço
2. Cadastrar aluno(a) de acordo com o seu objetivo de treino
3. Listar aluno(a) cadastrado
4. Consultar o aluno(a) cadastrado pelo CPF
5. Deletar aluno(a) cadastrado pelo CPF
6. Informar a quantidade de aluno(a) cadastrado(s)
7. Mostrar o Faturamento Mensal
'''

lista_aluno = [] # Armazena o cadastro dos aluno(a)
adicionar_preco = [] # Armazena o preço
faturamento_mensal = [] # Armazenal o faturamento mensal

# Tupla para criar uma tabela de quantidade de semanas x preço
lista_preco = ("1x semana", 95.00, "2x semana", 95.00, "3x semana", 90.00,
                "Trismestral", 85.00, "Semestral", 80.00, "Anual (consultar)", 00.00)

# Dicionário para auxiliar na escolha quantidade de aulas x preço
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


# Função para criar linha e texto
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *80)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *80)


# Função para ler apenas número inteiro e interrupção do teclado pelo usuário
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


# Função, onde pergunta se o usuário quer continuar com o programa
def resposta():
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        print("\033[32mSaindo...\33[m")


# Função que cria uma tabela de quantidade de semanas x preço
def tabela_preco():
    os.system("cls")
    titulo("TABELA DE PREÇOS".center(80))
    for c in range(0, len(lista_preco), 2):
        print(f"{lista_preco[c]:.<30} R$ {lista_preco[c+1]:>6.2f}".center(80))


# Função que cria um sub menu com condições de acordo com a opção selecionada
# Armazena os valores na lista adicionar_preco
# Armazena o fatuamento na lista faturamento_mensal
def menu_preco():
    totalPreco = 0
    print("\033[1;94m-\033[0;0m" *80)
    print("[1] 1x semana\n[2] 2x semana\n[3] 3x semana\n[4] Trismestral\n[5] Semestral\n[6] Anual (consultar valores)\n[7] Sair")
    print("\033[1;94m-\033[0;0m" *80)

    opcao = leiaInt("Digite a sua opção / plano: ")
    if opcao == 1:
        print("Você escolheu o plano 1x semana \033[32mR$ 95.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["100"][1]
        adicionar_preco.append(totalPreco)
        faturamento = totalPreco * 4
        faturamento_mensal.append(faturamento)
    elif opcao == 2:
        print("Você escolheu o plano 2x semana \033[32mR$ 190.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["101"][1]
        adicionar_preco.append(totalPreco)
        faturamento = totalPreco * 4
        faturamento_mensal.append(faturamento)
    elif opcao == 3:
        print("Você escolheu o plano 3x semana \033[32mR$ 270.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["102"][1]
        adicionar_preco.append(totalPreco)
        faturamento = totalPreco * 4
        faturamento_mensal.append(faturamento)
    elif opcao == 4:
        print("Você escolheu o plano Trimestral \033[32mR$ 00.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["103"][1]
        adicionar_preco.append(totalPreco)
        faturamento = totalPreco * 4
        faturamento_mensal.append(faturamento)
    elif opcao == 5:
        print("Você escolheu o plano Semestral \033[32mR$ 00.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["104"][1]
        adicionar_preco.append(totalPreco)
        faturamento = totalPreco * 4
        faturamento_mensal.append(faturamento)
    elif opcao == 6:
        print("Você escolheu o plano Anual (consultar) \033[32mR$ 00.00\33[m")
        totalPreco += menu_tabela_preco["tabela"]["105"][1]
        adicionar_preco.append(totalPreco)
        faturamento = totalPreco * 4
        faturamento_mensal.append(faturamento)
    elif opcao == 7:
        print("\033[32mSaindo da tabela de preços\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 7\33[m")


# Função para cadastrar um novo aluno(a)
def cadastrar_aluno():
    titulo("CADASTRO DE ALUNO(A)".center(80))
    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")

    lista_aluno.append((nome, idade, cpf, data_atual))
    sleep(0.5)
    print("\033[32mAluno(a) cadastro com sucesso\33[m")


# Função para listar / imprimir aluno(a) cadastrado
def listar_aluno():
    os.system("cls")
    titulo("LISTA DE ALUNO(A) CADASTRADO".center(80))
    print("ID".center(3), end='')
    print("Nome".center(20), end='')
    print("Idade".center(20), end='')
    print("CPF".center(20), end='')
    print("Registro".center(20))
    
    for indice_aluno in list(enumerate(lista_aluno, start=1)):

        indice = indice_aluno[0]
        aluno = indice_aluno[1]

        print(str(indice).center(3), end='')
        print(str(aluno[0]).center(20), end='')
        print(str(aluno[1]).center(20), end='')
        print(str(aluno[2]).center(20), end='')
        print(str(aluno[3]).center(20))

    print("\033[1;94m-\033[0;0m" *80)
    os.system("pause")


# Função para buscar aluno(a) cadastrado pelo CPF
def buscar_aluno():
    os.system("cls")
    termo = input("Informe o CPF do aluno(a) para buscar: ")
    print("\033[1;94m-\033[0;0m" *80)
    for cadastro_aluno in lista_aluno:
        nome, idade, cpf, data_atual = cadastro_aluno
        if cpf == termo:
            print(f"Nome: {nome}\nIdade: {idade}\nCPF: {cpf}\nRegistro: {data_atual}")
    print("\033[1;94m-\033[0;0m" *80)
    os.system("pause")


# Função para deletar aluno(a) cadastrado pelo CPF
def deletar_aluno():
    os.system("cls")
    termo = input("Informe o CPF do aluno(a) que deseja remover: ")
    print("\033[1;94m-\033[0;0m" *80)
    for cadastro_aluno in lista_aluno:
        nome, idade, cpf, data_atual = cadastro_aluno
        if cpf == termo:
            lista_aluno.remove((nome, idade, cpf, data_atual))
            print(f"CPF {cpf} removido\nData/hora: {data_atual}")
    print("\033[1;94m-\033[0;0m" *80)
    os.system("pause")


# Função para fechamento do plano selecionado
# Efetua o somatório total através da lista adicionar_preco
# Efetua o faturamento mensal através da variável valor_total
def fechar_plano():
    cadastrar_aluno()
    titulo("FECHAR PLANO DO ALUNO(A)".center(80))
    valor_total = sum(adicionar_preco)
    print(f"Registro: {data_atual}")
    sleep(0.5)
    print(f"Valor do plano \033[32mR$ {valor_total:.2f}\33[m")
    print(f"Mensalidade Total R$ \033[32m{(valor_total * 4):.2f}\33[m")
    print("\033[1;94m-\033[0;0m" *80)


# Função principal que executa todo processo
def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA PERSONAL TRAINER".center(80))
        print("\033[1;97m1 - Fechar Plano\n2 - Listar Aluno\n3 - Buscar Aluno\n4 - Deletar Aluno\n5 - Sair\033[0;0m")
        print("\033[1;94m-\033[0;0m" *80)
        print(f"Ao todo foram cadastrado(s) \033[32m{len(lista_aluno)}\33[m aluno(as)")
        print(f"Faturamento \033[32mR$ {sum(faturamento_mensal):.2f}\33[m")
        print("\033[1;94m-\033[0;0m" *80)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            tabela_preco()
            menu_preco()
            fechar_plano()
            resposta()
        elif opcao == 2:
            listar_aluno()
        elif opcao == 3:
            buscar_aluno()
        elif opcao == 4:
            deletar_aluno()
        elif opcao == 5:
            print("\033[32mSaindo do programa... Agradeço pela preferência\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 5\33[m")
    os.system("pause")

menu()
