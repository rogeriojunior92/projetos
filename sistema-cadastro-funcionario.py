# Importar Libs
import os 
import re
from datetime import datetime
from time import sleep

# Dicionário para armazenar o cadastro
cadastro = dict()
lista_cadastro = []
limite_cadastro = 20

data = datetime.now()
data_atual = data.strftime('%d/%m/%Y - %H-%M')


# Função para criar linha e texto
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


# Função para ler número inteiro e interrupção do teclado pelo usuário
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


# Função para criar um arquivo novo
def novo_arquivo():
    os.system('cls')
    try:
        with open("cadastro_funcionario.txt", "wt+") as arquivo:
            arquivo.close()
    except:
        print("\033[31mOcorreu um erro na criação do arquivo\33[m")
    else:
        print("\033[32mArquivo criado com sucesso\33[m")
    os.system('pause')


# Função para cadastrar um novo funcionário e armazenar os dados na lista
def novo_cadastro():
    os.system('cls')

    limite_cadastro_funcionarios = len(lista_cadastro)
    if limite_cadastro_funcionarios < limite_cadastro:
        
        print(f"Horário de Registro: {data_atual}")
        cadastro['Nome'] = input("Nome: ")
        cadastro['CPF'] = input("CPF: ")
        cadastro['Ano de Nascimento'] = int(input("Ano de Nascimento: "))
        cadastro['Idade'] = datetime.now().year - cadastro['Ano de Nascimento']
        cadastro['Salário'] = float(input("Salário: R$ "))

        while True:
            cadastro['Sexo'] = input("Sexo: [M/F] ").upper()[0]
            if cadastro['Sexo'] in "MF":
                break
            print("ERRO! Digite apenas M ou F")
        
        cadastro['CTPS'] = int(input("Nº CTPS (0 não tem): "))
        if cadastro['CTPS'] == 0:
            cadastro['Aposentadoria'] = cadastro['Idade'] + 35
    
        lista_cadastro.append(cadastro.copy())
        print("\033[32mCadastrado com sucesso\33[m")
    
    else:
        print(f"\033[31mERRO! Não é possível cadastrar mais contatos. Limite de {limite_cadastro} atingido\33[m")
    os.system('pause')


# Função para imprimir os funcionários cadastrados
def imprimir_cadastro():
    os.system('cls')
    print("ID".center(3), end='')
    print("Nome".center(20), end='')
    print("CPF".center(20), end='')
    print("Ano de Nascimento".center(20), end='')
    print("Idade".center(20), end='')
    print("Salário".center(20), end='')
    print("Sexo".center(20), end='')
    print("CTPS".center(20), end='')
    print("Aposentadoria".center(20))

    for indice_cadastro in list(enumerate(lista_cadastro)):

        indices = indice_cadastro[0]
        cadastro = indice_cadastro[1]

        print(str(indices).center(3), end='')
        print(str(cadastro['Nome']).center(20), end='')
        print(str(cadastro['CPF']).center(20), end='')
        print(str(cadastro['Ano de Nascimento']).center(20), end='')
        print(str(cadastro['Idade']).center(20), end='')
        print(str(cadastro['Salário']).center(20), end='')
        print(str(cadastro['Sexo']).center(20), end='')
        print(str(cadastro['CTPS']).center(20), end='')
        print(str(cadastro['Aposentadoria']).center(20))


# Função para buscar cadastro pelo CPF
def buscar_cadastro():
    os.system('cls')
    titulo("BUSCAR CADASTRO DE FUNCIONÁRIO".center(50))
    termo = input("Informe o nº CPF para localizar o cadastro: ")
    for lista in lista_cadastro:
        cpf = lista['CPF']
        print("\033[1;94m-\033[0;0m" *50)
        if cpf == termo:
            sleep(0.5)
            print(f"Nome: {lista['Nome']}\nCPF: {lista['CPF']}\nAno Nascimento: {lista['Ano de Nascimento']}\nIdade: {lista['Idade']}\nSalário: {lista['Salário']}\nSexo: {lista['Sexo']}\nCTPS: {lista['CTPS']}\nAposentadoria: {lista['Aposentadoria']}\nHorário de Registro: {data_atual}")
    os.system('pause')


# Função para deletar cadastro pelo CPF
def deletar_cadastro():
    os.system('cls')
    titulo("DELETAR CADASTRO DE FUNCIONÁRIO".center(50))
    termo = input("Informe o nº CPF para deletar o cadastro: ")
    for lista in lista_cadastro:
        cpf = lista['CPF']
        print("\033[1;94m-\033[0;0m" *50)
        if cpf == termo:
            sleep(0.5)
            lista_cadastro.remove(lista)
        print(f"CPF \033[32m{termo}\33[m removido com sucesso")
    os.system('pause')


# Função para atualizar cadastro pelo CPF
def atualizar_cadastro():
    os.system('cls')
    titulo("ATUALIZAR CADASTRO DE FUNCIONÁRIO".center(50))
    termo = input("Informe o nº CPF para atualizar o cadastro: ")
    for lista in lista_cadastro:        
        cpf = lista['CPF']
        print("\033[1;94m-\033[0;0m" *50)
        if cpf == termo:
            sleep(0.5)
            print(f"Nome: {lista['Nome']}\nCPF: {lista['CPF']}\nAno Nascimento: {lista['Ano de Nascimento']}\nIdade: {lista['Idade']}\nSalário: {lista['Salário']}\nSexo: {lista['Sexo']}\nCTPS: {lista['CTPS']}\nAposentadoria: {lista['Aposentadoria']}")
            print("\033[1;94m-\033[0;0m" *50)

            while True:
                titulo("MENU DE ATUALIZAÇÃO CADASTRAL".center(50))
                print("1 - Nome\n2 - CPF\n3 - Ano de Nascimento\n4 - Idade\n5 - Salário\n6 - Sexo\n7 - CTPS\n8 - Sair")
                print("\033[1;94m-\033[0;0m" *50)

                opcao = leiaInt("Digite a sua opção que deseja alterar: ")
                if opcao == 1:
                    novo_nome = input("Informe o novo Nome para alteração: ")
                    if novo_nome in lista_cadastro[0]['Nome']:
                        print(f"Nao existe \033[31m{novo_nome}\33[m na lista")
                    else:
                        lista_cadastro[0]['Nome'] = novo_nome
                        print(f"Nome \033[32m{novo_nome}\33[m alterado com sucesso!")

                elif opcao == 2:
                    novo_cpf = input("Informe o novo CPF para alteração: ")
                    if novo_cpf in lista_cadastro[0]['CPF']:
                        print(f"Nao existe \033[31m{novo_cpf}\33[m na lista")
                    else:
                        lista_cadastro[0]['CPF'] = novo_cpf
                        print(f"CPF \033[32m{novo_cpf}\33[m alterado com sucesso!")

                elif opcao == 3:
                    novo_ano_nascimento = input("Informe o novo Ano de Nascimento para alteração: ")
                    if novo_ano_nascimento in lista_cadastro[0]['Ano de Nascimento']:
                        print(f"Nao existe \033[31m{novo_ano_nascimento}\33[m na lista")
                    else:
                        lista_cadastro[0]['Ano de Nascimento'] = novo_ano_nascimento
                        print(f"Ano de Nascimento \033[32m{novo_ano_nascimento}\33[m alterado com sucesso!")

                elif opcao == 4:
                    nova_idade = input("Informe a nova Idade para alteração: ")
                    if nova_idade in lista_cadastro[0]['Idade']:
                        print(f"Nao existe \033[31m{nova_idade}\33[m na lista")
                    else:
                        lista_cadastro[0]['Idade'] = nova_idade
                        print(f"Idade \033[32m{nova_idade}\33[m alterado com sucesso!")
                
                elif opcao == 5:
                    novo_salario = float(input("Informe o novo Salário para alteração: R$ "))
                    if novo_salario in lista_cadastro[0]['Salário']:
                        print(f"Nao existe \033[31m{novo_salario}\33[m na lista")
                    else:
                        lista_cadastro[0]['Salário'] = novo_salario
                        print(f"Novo salário \033[32mR$ {lista_cadastro}\33[m alterado com sucesso!")

                elif opcao == 6:
                    novo_sexo = input("Informe o novo Sexo para alteração: [M/F] ").upper()[0]
                    if novo_sexo in lista_cadastro[0]['Sexo']:
                        print(f"Nao existe \033[31m{novo_sexo}\33[m na lista")
                    else:
                        print(f"Sexo \033[32mR$ {novo_sexo}\33[m alterado com sucesso!")

                elif opcao == 7:
                    novo_ctps = input("Informe o novo CTPS para alteração: ")
                    if novo_ctps in lista_cadastro[0]['CTPS']:
                        print(f"Nao existe \033[31m{novo_ctps}\33[m na lista")
                    else:
                        lista_cadastro[0]['CTPS'] = novo_ctps
                        print(f"CTPS \033[32mR$ {novo_ctps}\33[m alterado com sucesso!")

                elif opcao == 8:
                    print("\033[32mSaindo do programa... Até logo!\33[m")
                    break
                else:
                    print("\033[31mOpção inválida. Digite entre 1 e 9\33[m")
    os.system('pause')


# Função que executa todo o processo
def menu():
    os.system('cls')
    while True:
        titulo("MENU CADASTRO DE FUNCIONÁRIO".center(50))
        print("1 - Novo Arquivo\n2 - Novo Cadastro\n3 - Imprimir Cadastro\n4 - Buscar Cadastro\n5 - Deletar Cadastro\n6 - Atualizar Cadastro\n7 - Sair")
        print("\033[1;94m-\033[0;0m" *50)
        print(f"Total de funcionário(s) \033[32m{len(lista_cadastro)}\33[m cadastro(s)")
        print(f"Limite de funcionários para cadastro \033[31m{limite_cadastro}\33[m")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            novo_arquivo()
        elif opcao == 2:
            novo_cadastro()
        elif opcao == 3:
            imprimir_cadastro()
        elif opcao == 4:
            buscar_cadastro()
        elif opcao == 5:
            deletar_cadastro()
        elif opcao == 6:
            atualizar_cadastro()
        elif opcao == 7:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 7\33[m")

menu()
