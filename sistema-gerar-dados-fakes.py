import pandas as pd
from faker import Faker

lista_dados = []
fake = Faker()


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
    for c in range(100):
        nome = fake.name()
        endereco = fake.address()
        email = fake.email()

        lista_dados.append((nome, endereco, email))
    return c


# Função para criar relatório excel
# Também é possível informar a quantidade de relatórios que deseja gerar
def gerar_relatorio_excel():
    titulo("GERAR RELATÓRIO EXCEL".center(50))
    relatorios = int(input("Quantos relatórios? "))
    for c in range(0, relatorios):
        try:
            df = pd.DataFrame(lista_dados, columns=["Nome", "Endereco", "E-mail"])
            df.to_excel(f"dados_fake_{c+1}.xlsx", index=False)
        except:
            print("\033[31mOcorreu na criação do relatório\33[m")
        else:
            print("\033[32mRelatório criado com sucesso\33[m")


# Função principal que executa todo o processo
def menu():
    while True:
        titulo("SISTEMA PARA CRIAR DADOS FAKES".center(50))
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
