import os
import pandas as pd
from time import sleep
from faker import Faker

locale = 'pt-BR'
lista_dados = []
fake = Faker(locale)


# Função para criar linha e texto (título)
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


# Função que gera dados fakes
def gerar_dados_faker():
    os.system("cls")
    titulo("GERADOR DE DADOS FAKES".center(50))
    try:
        for c in range(1):
            nome = fake.name()
            data = fake.date()
            ano = fake.year()
            cidade = fake.city()
            estado = fake.state()
            telefone = fake.phone_number()
            email = fake.email()
            trabalho = fake.job()

            lista_dados.append((nome, data, ano, cidade, estado, telefone, email, trabalho))
            print(lista_dados)
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na criação dos Dados Fakes\33[m")
    else:
        sleep(0.5)
        print("\033[32mDados Fakes criado com sucesso\33[m")
    os.system("pause")

    return c
    

# Função para criar relatório excel com quantidade de relatórios desejado
def gerar_relatorio_excel():
    os.system("cls")
    titulo("GERAR RELATÓRIO EXCEL".center(50))
    relatorios = int(input("Deseja gerar quantos relatórios Excel? "))
    for c in range(0, relatorios):
        try:
            df = pd.DataFrame(lista_dados, columns=["nome", "data_nasc", "ano", "cidade", "estado", "sigla", "telefone", "e-mail", "cargo"])
            df.to_excel(f"dados_fake_{c+1}.xlsx", index=False)
        except:
            sleep(0.5)
            print("\033[31mOcorreu na criação do relatório\33[m")
        else:
            sleep(0.5)
            print("\033[32mRelatório criado com sucesso\33[m")
    os.system("pause")


# Função principal que executa todo o processo
def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA DADOS FAKES".center(50))
        print("1 - Criar Dataset\n2 - Gerar Relatório\n3 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            gerar_dados_faker()
        elif opcao == 2:
            gerar_relatorio_excel()
        elif opcao == 3:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 3\33[m")

menu()
