import os
from time import sleep
from datetime import datetime
import pandas as pd


lista_veiculo = []
limite_vagas = 10

    
def titulo(txt):
    print("\033[36m-\033[0;0m" *105)
    print("\033[36m"+txt+"\033[0;0m")
    print("\033[36m-\033[0;0m" *105)


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num


def novo_cadastro():
    os.system("cls")

    limite_vagas_veiculos = len(lista_veiculo)
    if limite_vagas_veiculos < limite_vagas:
        
        data = datetime.now()
        data_atual = data.strftime("%d/%m/%Y - %H:%M")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        proprietario = input("Proprietário(a): ")

        lista_veiculo.append((marca, modelo, placa, proprietario, data_atual))
        sleep(0.5)
        print("\033[32mVeículo cadastrado com sucesso\33[m")

    else:
        sleep(0.5)
        print(f"\033[31mERRO! Não é possível cadastrar mais véiculos. Limite de {limite_vagas} atingido\33[m")
    os.system("pause")
    

def imprimir_cadastro():
    os.system("cls")
    print("\033[36m-\033[0;0m" *105)
    print("ID".center(3), end='')
    print("Marca".center(20), end='')
    print("Modelo".center(20), end='')
    print("Placa".center(20), end='')
    print("Proprietário(a)".center(20), end='')
    print("Data".center(20))

    for indice_veiculo in list(enumerate(lista_veiculo, start=1)):

        indice = indice_veiculo[0]
        veiculo = indice_veiculo[1]

        print(str(indice).center(3), end='')
        print(str(veiculo[0]).center(20), end='')
        print(str(veiculo[1]).center(20), end='')
        print(str(veiculo[2]).center(20), end='')
        print(str(veiculo[3]).center(20), end='')
        print(str(veiculo[4]).center(20))
    print("\033[36m-\033[0;0m" *105)
    os.system("pause")


def buscar_cadastro():
    os.system("cls")
    termo = input("Informe a placa do veículo para consultar: ")
    print("\033[36m-\033[0;0m" *105)
    for placa_veiculo in lista_veiculo:
        marca, modelo, placa, proprietario, data_atual = placa_veiculo
        if placa == termo:
            sleep(0.5)
            print(f"Marca: {marca}\nModelo: {modelo}\nPlaca: {placa}\nProprietário(a): {proprietario}\nData: {data_atual}")
    print("\033[36m-\033[0;0m" *105)
    os.system("pause")


def deletar_cadastro():
    os.system("cls")
    termo = input("Informa a placa do veículo que deseja deletar: ")
    print("\033[36m-\033[0;0m" *105)
    for placa_veiculo in lista_veiculo:
        marca, modelo, placa, proprietario, data_atual = placa_veiculo
        if placa == termo:
            lista_veiculo.remove((marca, modelo, placa, proprietario, data_atual))
            sleep(0.5)
            print(f"Dados removido com sucesso\nPlaca: {placa}")
    print("\033[36m-\033[0;0m" *105)
    os.system("pause")


def gerar_relatorio():
    titulo("CRIANDO RELATÓRIO EXCEL".center(105))
    try:
        df = pd.DataFrame(lista_veiculo, columns=["Marca", "Modelo", "Placa", "Proprietario", "Data"])
        df.to_excel("veiculos.xlsx")
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na criação do relatório\33[m")
    else:
        sleep(0.5)
        print("\033[32mRelatório criado com sucesso.\33[m")
    print("\033[36m-\033[0;0m" *105)


def menu():
    while True:
        titulo("SISTEMA DE ESTACIONAMENTO PYTHON".center(105))
        print("1 - NOVO CADASTRO\n2 - LISTAR CADASTRO\n3 - BUSCAR CADASTRO\n4 - DELETAR CADASTRO\n5 - GERAR RELATÓRIO\n6 - SAIR")
        print("\033[36m-\033[0;0m" *105)
        print(f"Ao todo foram cadastrados \033[32m{len(lista_veiculo)}\33[m veículo(s)")
        print("\033[36m-\033[0;0m" *105)
        print(f"Limite de vagas \033[32m{limite_vagas}\33[m")
        print(f"Vagas ocupadas \033[31m{len(lista_veiculo) / limite_vagas * 100}% \33[m")
        print("\033[36m-\033[0;0m" *105)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            novo_cadastro()
        elif opcao == 2:
            imprimir_cadastro()
        elif opcao == 3:
            buscar_cadastro()
        elif opcao == 4:
            deletar_cadastro()
        elif opcao == 5:
            gerar_relatorio()
        elif opcao == 6:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")

menu()
