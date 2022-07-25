from datetime import date, datetime
import os

data = datetime.now()
data_atual = data.strftime("%d/%m/%Y %H:%M")

'''
Sistema de Oftalmologia em andamento
'''
preco_exames = ("Tomografia de Coerência Óptica", 1000, "Retinografia", 800, "Topografia", 900, "Paquinetrua", 700)

lista_consulta = []
valor_exame = []

nome_paciente = input("Nome do Paciente: ")
nome_repecao = input("Nome da Recepcionista: ")


def titulo(txt):
    print("\033[36m-\033[0;0m" *85)
    print("\033[1;46m"+txt+"\033[1;0m")
    print("\033[36m-\033[0;0m" *85)


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
        resp = input("Deseja realizar outro exame? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("033[31mERRO! Digite apenas S ou N\33[m")
    if resp == "N":
        print("\033[32mSaindo do menu de exames\33[m")


def novo_arquivo():
    os.system("cls")
    try:
        with open("consulta_oftalmologia.txt", "wt+") as arquivo:
            arquivo.close()
    except:
        print("\033[31mOcorreu um erro na criação do arquivo\33[m")
    else:
        print("\033[32mArquivo criado com sucesso\33[m")
    os.system("pause")


def novo_cadastro():
    os.system("cls")
    nome = input("Nome: ")
    data_nasc = input("Data de Nascimento: ")
    cpf = input("CPF: ")

    lista_consulta.append((nome, data_nasc, cpf, data_atual))

    os.system("pause")


def lista_exames():
    os.system("cls")
    titulo("LISTA DE EXAMES".center(85))
    for c in range(0, len(preco_exames), 2):
        print(f"\033[1;97m{preco_exames[c]:.<45} R$ {preco_exames[c+1]:>6.2f}\033[1;0m")
    print("\033[36m-\033[0;0m" *85)
    print("\033[1;97m1 - Tomografia de Coerência Óptica\n2 - Retinografia\n3 - Topografia\n4 - Paquinetrua\n5 - Sair\033[1;0m")
    print("\033[36m-\033[0;0m" *85)

    opcao = leiaInt("Digite a sua opção: ")
    print("\033[36m-\033[0;0m" *85)
    if opcao == 1:
        print(f"Olá, {nome_paciente}. Seja bem-vindo(a) a clinica de Oftalmologia\nMeu nome é {nome_repecao}, será um prazer em atendê-lo(a)\nSeu exame será Tomografia de Coerência Óptica\nPor favor, informar os dados para cadastro:")
        print("\033[36m-\033[0;0m" *85)
        novo_cadastro()
        resposta()
    elif opcao == 2:
        print(f"Olá, {nome_paciente}. Seja bem-vindo(a) a clinica de Oftalmologia\nMeu nome é {nome_repecao}, será um prazer em atendê-lo(a)\nSeu exame será Retinografia\nPor favor, informar os dados para cadastro:")
        print("\033[36m-\033[0;0m" *85)
        novo_cadastro()
        resposta()
    elif opcao == 3:
        print(f"Olá, {nome_paciente}. Seja bem-vindo(a) a clinica de Oftalmologia\nMeu nome é {nome_repecao}, será um prazer em atendê-lo(a)\nSeu exame será Topografia\nPor favor, informar os dados para cadastro:")
        print("\033[36m-\033[0;0m" *85)
        novo_cadastro()
        resposta()
    elif opcao == 4:
        print(f"Olá, {nome_paciente}. Seja bem-vindo(a) a clinica de Oftalmologia\nMeu nome é {nome_repecao}, será um prazer em atendê-lo(a)\nSeu exame será Paquinetrua\nPor favor, informar os dados para cadastro:")
        print("\033[36m-\033[0;0m" *85)
        novo_cadastro()
        resposta()
    elif opcao == 5:
        print("Saindo da lista de exames")
        menu()
    os.system("pause")


def listar_cadastro():
    os.system("cls")
    titulo("LISTA DE CADASTRADO PARA CONSULTA".center(85))
    print("ID".center(3), end='')
    print("Nome".center(20), end='')
    print("Data Nascimento".center(20), end='')
    print("CPF".center(20), end='')
    print("Data / Hora".center(20))

    for indice_consulta in list(enumerate(lista_consulta, start=1)):

        indice = indice_consulta[0]
        consulta = indice_consulta[1]

        print(str(indice).center(3), end='')
        print(str(consulta[0]).center(20), end='')
        print(str(consulta[1]).center(20), end='')
        print(str(consulta[2]).center(20), end='')
        print(str(consulta[3]).center(20))
    print("\033[36m-\033[0;0m" *85)


def buscar_cadastro():
    os.system("cls")
    termo = input("Informe o CPF para buscar o cadastr do paciente: ")
    for buscar_cpf in lista_consulta:
        nome, data_nasc, cpf, data_atual = buscar_cpf
        if cpf == termo:
            print("\033[36m-\033[0;0m" *85)
            print(f"Nome: {nome}\nData Nascimento: {data_nasc}\nCPF: {cpf}\nData/Hora: {data_atual}")
            print("\033[36m-\033[0;0m" *85)
    os.system("pause")


def deletar_cadastro():
    os.system("cls")
    termo = input("Informe o CPF para deletar o cadastro: ")
    for buscar_cpf in lista_consulta:
        nome, data_nasc, cpf, data_atual = buscar_cpf
        if cpf == termo:
            lista_consulta.remove((nome, data_nasc, cpf, data_atual))
        print(f"Cadastro removido com sucesso\nCPF: {cpf}")
    os.system("pause")


def valor_consulta():
    os.system("cls")
    titulo("VALOR DA CONSULTA".center(85))
    print(f"Registro da Saída: {data_atual}")
    total = sum(valor_exame)
    print(f"Paciente {nome_paciente}, valor da consulta R$ {total:.2f}")
    print("\033[36m-\033[0;0m" *85)
    os.system("pause")


def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA DE OFTALMOLOGIA".center(85))
        print("\033[1;97m1 - Lista de Exames\n2 - Novo Arquivo\n3 - Listar Cadastrado\n4 - Buscar Cadastro\n5 - Deletar Cadastro\n6 - Valor da Consulta\n7 - Sair\033[1;0m")
        print("\033[36m-\033[0;0m" *85)
        print(f"Ao todo foram cadastro(s) \033[32m{len(lista_consulta)}\33[m exame(s)")
        print("\033[36m-\033[0;0m" *85)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            lista_exames()
        elif opcao == 2:
            novo_arquivo()
        elif opcao == 3:
            listar_cadastro()
        elif opcao == 4:
            buscar_cadastro()
        elif opcao == 5:
            deletar_cadastro()
        elif opcao == 6:
            valor_consulta()
        elif opcao == 7:
            print("\033[32mSaindo do programa... Agradecemos pela preferência!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")
    os.system("pause")

menu()
