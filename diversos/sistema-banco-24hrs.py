# Imports libs
import os
from time import sleep 
from datetime import datetime
from random import randint

# Dicionários para criar os dados da conta PF e PJ
conta = {}
conta_pj = {}
# Listas para armazenar os dados da conta PF e PJ
lista_conta = []
lista_conta_pj = []

# Manipulação de datas
data = datetime.now()
data_atual = data.strftime('%d/%m/%Y - %H:%M:%S')


# Função para criar linha + texto
def titulo(txt):
    print("\033[36m-\33[m" *85)
    print("\033[36m"+txt+"\33[m")
    print("\033[36m-\33[m" *85)


# Função para trativa de erros, para aceitar apenas números inteiros e exceção, caso o usuário não digitar nenhum número (Exemplo: Enter)
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


# Função para cadastrar conta PF e PJ
def criar_conta():
    os.system('cls')
    while True:
        titulo("BEM-VINDO AO BANCO 24HRs - ABERTURA DE CONTA".center(85))
        print("1 - Pessoa Física\n2 - Pessoa Juridica\n0 - Sair")
        print("\033[36m-\33[m" *85)

        opcao = leiaInt("Digite a sua opção: ")
        # Opção 1: Para cadastrar uma nova conta Pessoa Fisica
        if opcao == 1:
            os.system('cls')
            titulo("ABERTURA DE CONTA - PESSOA FISICA".center(85))
            conta["Numero"] = int(input("Nº da Conta: "))
            # Iteração na lista_conta para validar a conta existente
            # Caso existir o mesmo número de conta no sistema, não será cadastrado.
            for pf in lista_conta:
                if pf['Numero'] == conta["Numero"]:
                    sleep(0.5)
                    print("\033[31mJá existe essa conta no sistema\33[m")
                    return
            else:
                conta["Titular"] = input("Titular: ")
                conta["Saldo"] = float(input("Saldo: R$ "))
                conta["Limite"] = float(input("Limite: R$ "))

            # Lista para armazenar o cadastro de Pessoa Fisica através do dicionário
            lista_conta.append(conta.copy())
            sleep(0.5)
            print("\033[32mConta de Pessoa Física cadastrado com sucesso\33[m")
        
        elif opcao == 2:
            # Opção 1: Para cadastrar uma nova conta Pessoa Juridica
            os.system('cls')
            titulo("ABERTURA DE CONTA - PESSOA JURIDICA".center(85))
            conta_pj['Numero'] = int(input("Nº da Conta: "))
            # Iteração na lista_conta_pj para validar a conta existente
            # Caso existir o mesmo número de conta no sistema, não será cadastrado.
            for pj in lista_conta_pj:
                if pj['Numero'] == conta_pj["Numero"]:
                    sleep(0.5)
                    print("\033[31mJá existe essa conta no sistema\33[m")
                    return
            else:
                conta_pj['CNPJ'] = input("Digte o CNPJ: ")
                conta_pj['Titular'] = input("Titular: ")
                conta_pj['Saldo'] = float(input("Saldo: R$ "))
                conta_pj['Limite'] = float(input("Limite: R$ "))

            # Lista para armazenar o cadastro de Pessoa Juridica através do dicionário
            lista_conta_pj.append(conta_pj.copy())
            sleep(0.5)
            print("\033[32mConta de Pessoa Juridica cadastrado com sucesso\33[m")

        elif opcao == 0:
            sleep(0.5)
            print("\033[32mSaindo da opção de Abertura de Conta!\33[m")
            break
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 0 e 3\33[m")
    os.system('pause')


# Função para consultar as contas existentes PF e PJ
def consultar_conta():
    os.system('cls')
    while True:
        titulo("BEM-VINDO AO BANCO 24HRs - CONTAS CADASTRADAS".center(85))
        print("1 - Pessoa Física\n2 - Pessoa Juridica\n0 - Sair")
        print("\033[36m-\33[m" *85)

        opcao = leiaInt("Digite a sua opção: ")
        # Opção 1: Para consultar cadastro da conta Pessoa Física
        if opcao == 1:
            os.system('cls')
            titulo("CONTAS CADASTRADAS - PESSOA FÍSICA".center(85))
            print(f"{'Nº':^4}{'Nº CONTA':^20}{'TITULAR':^20}{'SALDO':^20}{'LIMITE':^20}")
            # Iteração na lista_conta, retorna as informações com indice.
            for i, lista in enumerate(lista_conta):
                sleep(0.5)
                print(f"{i:^4}{lista['Numero']:^20}{lista['Titular']:^20}{lista['Saldo']:^20.2f}{lista['Limite']:^20.2f}")

        # Opção 2: Para consultar cadastro da conta Pessoa Juridica
        elif opcao == 2:
            os.system('cls')
            titulo("CONTAS CADASTRADAS - PESSOA JURIDICA".center(85))
            print(f"{'Nº':^4}{'Nº CONTA':^20}{'CNPJ':^20}{'TITULAR':^20}{'SALDO':^20}{'LIMITE':^20}")
            # Iteração na lista_conta_pj, retorna as informações com indice.
            for i, lista_cnpj in enumerate(lista_conta_pj):
                sleep(0.5)
                print(f"{i:^4}{lista_cnpj['Numero']:^20}{lista_cnpj['CNPJ']:^20}{lista_cnpj['Titular']:^20}{lista_cnpj['Saldo']:^20.2f}{lista_cnpj['Limite']:^20.2f}")

        elif opcao == 0:
            sleep(0.5)
            print("\033[32mSaindo da opção de Listar Contas Cadastradas!\33[m")
            break
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 0 e 3\33[m")
    os.system('pause')
    

# Função para sacar valores da conta
def sacar_conta():
    os.system('cls')
    while True:
        titulo("BEM-VINDO AO BANCO 24HRs - SACAR".center(85))
        print("1 - Pessoa Física\n2 - Pessoa Juridica\n0 - Sair")
        print("\033[36m-\33[m" *85)

        opcao = leiaInt("Digite a sua opção: ")
        # Opção 1: Para para sacar valores da conta Pessoa Fisica
        if opcao == 1:
            termo = int(input("Favor, informe o número da conta que deseja sacar: "))        
            titulo("RESUMO DA CONTA - PESSOA FÍSICA".center(85))
            # Iteração na lista_conta
            # Variável num = lista['Numero'] que busca o chave Número da lista_conta 
            for lista in lista_conta:
                num = lista['Numero']
                if num == termo:
                    print(f"Numero: {lista['Numero']}\nTitular: {lista['Titular']}\nSaldo: {lista['Saldo']:.2f}\nLimite: {lista['Limite']:.2f}")
                    print("\033[36m-\33[m" *85)
                    # Variável que o usuário determina o valor para ser sacado
                    saque = float(input("Qual o valor deseja sacar: R$ "))
                    print("\033[36m-\33[m" *85)
                    # Dentro da iteração a lista['Saldo'] irá substrair o saldo na conta com a varíavel "saque" que o usuário determina o valor para ser sacado
                    lista['Saldo'] -= saque
                    sleep(0.5)
                    print(f"Horário: {data_atual}")
                    print(f"Valor do Saque R$ -{saque:.2f}")
                    print(f"Saldo Total R$ {lista['Saldo']:.2f}")
                else:
                    sleep(0.5)
                    print(f"\033[31mNúmero de conta {termo} inexistente\33[m")

        # Opção 2: Para para sacar valores da conta Pessoa Juridica
        elif opcao == 2:
            os.system('cls')
            termo = int(input("Favor, informe o número da conta que deseja sacar: "))
            titulo("RESUMO DA CONTA - PESSOA JURIDICA".center(85))
            # Iteração na lista_conta_pj
            for lista_cnpj in lista_conta_pj:
                # Variável num_cnpj = lista_cnpj['Numero'] busca a chave Número da lista_conta_pj 
                num_cnpj = lista_cnpj['Numero']
                if num_cnpj == termo:
                    print(f"Numero: {lista_cnpj['Numero']}\nCNPJ: {lista_cnpj['CNPJ']}\nTitular: {lista_cnpj['Titular']}\nSaldo: {lista_cnpj['Saldo']:.2f}\nLimite: {lista_cnpj['Limite']:.2f}")
                    print("\033[36m-\33[m" *85)
                    # Variável saque_cnpj onde o usuário determina o valor para ser sacado
                    saque_cnpj = float(input("Qual o valor que deseja sacar: R$ "))
                    print("\033[36m-\33[m" *85)
                    # Dentro da iteração a lista_cnpj['Numero'] irá substrair o saldo na conta com a varíavel "saque_cnpj" que o usuário determina o valor para ser sacado
                    lista_cnpj['Saldo'] -= saque_cnpj
                    sleep(0.5)
                    print(f"Horário: {data_atual}")
                    print(f"Valor do Saque R$ -{saque_cnpj:.2f}")
                    print(f"Saldo Total R$ {lista_cnpj['Saldo']:.2f}")
                else:
                    sleep(0.5)
                    print(f"\033[31mNúmero de conta {termo} inexistente\33[m")

        elif opcao == 0:
            print("\033[32mSaindo da opção de Saque\33[m")
            break
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 0 e 3\33[m")
    print("\033[36m-\33[m" *85)
    os.system('pause')


# Função para depositar valor na conta
def depositar():
    os.system('cls')
    while True:
        titulo("BEM-VINDO AO BANCO 24HRs - DEPOSITAR".center(85))
        print("1 - Pessoa Física\n2 - Pessoa Jurídica\n0 - Sair")
        print("\033[36m-\33[m" *85)

        opcao = leiaInt("Digite a sua opção: ")
        # Opção 1: Para para depositar valores da conta Pessoa Fisica
        if opcao == 1:
            termo = int(input("Favor, informe o número da conta que deseja depositar: "))
            # Iteração na lista_conta
            for lista in lista_conta:
                # Variável num = lista['Numero'] busca a chave Número da lista_conta
                num = lista['Numero']
                if num == termo:
                    # Variável depositar onde o usuário determina o valor para ser depositado
                    depositar = float(input("Quanto deseja depositar? R$ "))
                    # Dentro da iteração a lista["Saldo"] irá somar o saldo na conta com a varíavel "depositar" que o usuário determina o valor para ser sacado
                    lista["Saldo"] += depositar
                    sleep(0.5)
                    print(f"Horário: {data_atual}")
                    print(f"Saldo Total R$ {lista['Saldo']:.2f}")
                else:
                    sleep(0.5)
                    print(f"\033[31mNúmero de conta {termo} inexistente\33[m")
        
        # Opção 2: Para para depositar valores da conta Pessoa Juridica
        elif opcao == 2:
            os.system("cls")
            termo = int(input("Favor, informe o número da conta que deseja depoistar: "))
            # Iteração na lista_conta_pj
            for lista_cnpj in lista_conta_pj:
                # Variável num_cnpj = lista_cnpj['Numero'] busca a chave Número da lista_conta_pj
                num_cnpj = lista_cnpj['Numero']
                if num_cnpj == termo:
                    # Variável depositar_cnpj onde o usuário determina o valor para ser depositado
                    depositar_cnpj = float(input("Quanto deseja depositar? R$ "))
                    # Dentro da iteração a lista_cnpj['Numero'] irá somar o saldo na conta com a varíavel "depositar_cnpj" que o usuário determina o valor para ser sacado
                    lista_cnpj['Saldo'] += depositar_cnpj
                    sleep(0.5)
                    print(f"Horário: {data_atual}")
                    print(f"Saldo Total R$ {lista_cnpj['Saldo']:.2f}")
                else:
                    sleep(0.5)
                    print(f"\033[31mNúmero de conta {termo} inexistente\33[m")

        elif opcao == 0:
            print("\033[32mSaindo da opção de Depositar\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 0 e 3\33[m")
    print("\033[36m-\33[m" *85)
    os.system('pause')


# Função que exibe o extrato da conta
def extrato():
    os.system('cls')
    while True:
        titulo("BEM-VINDO AO BANCO 24HRs - EXTRATO".center(85))
        print("1 - Pessoa Física\n2 - Pessoa Juridica\n0 - Sair")
        print("\033[36m-\33[m" *85)

        opcao = leiaInt("Digite a sua opção: ")
        # Opção 1: Para para consultar extrato da conta Pessoa Fisica
        if opcao == 1:
            # Variável que busca o cadastro da conta PF através do número da conta
            termo = int(input("Favor, informe o número da conta que deseja consultar o extrato PF: "))
            # Iteração com a lista_conta
            for lista in lista_conta:
                # Variável num = lista['Numero'] busca a chave Número da lista_conta
                num = lista['Numero']
                # Se o número da conta for igual o número do termo digitado, irá trazer os dados da conta registrado
                if num == termo:
                    titulo("RESUMO DO EXTRATO - PESSOA FÍSICA".center(85))
                    print(f"Horário: {data_atual}")
                    sleep(0.5)
                    # Imprime os dados da conta registrado
                    print(f"Número: {lista['Numero']}\nTitular: {lista['Titular']}\nSaldo: R$ {lista['Saldo']:.2f}\nLimite: R$ {lista['Limite']:.2f}")
                else:
                    sleep(0.5)
                    print(f"\033[31mNúmero de conta {termo} inexistente\33[m")
        
        # Opção 1: Para para consultar extrato da conta Pessoa Juridica
        elif opcao == 2:
            os.system("cls")
            # Variável que busca o cadastro da conta PJ através do número da conta
            termo = int(input("Favor, informe o número da conta que deseja consultar extrato PJ: "))
            # Iteração com a lista_conta_pj
            for lista_cnpj in lista_conta_pj:
                # Variável num_cnpj = lista_cnpj['Numero'] busca a chave Número da lista_conta_pj
                num_cnpj = lista_cnpj['Numero']
                # Se o número da conta for igual o número do termo digitado, irá trazer os dados da conta registrado
                if num_cnpj == termo:
                    titulo("RESUMO DO EXTRATO - PESSOA JURIDICA".center(85))
                    print(f"Horário: {data_atual}")
                    sleep(0.5)
                    # Imprime os dados da conta registrado
                    print(f"Número: {lista_cnpj['Numero']}\nCNPJ: {lista_cnpj['CNPJ']}\nTitular: {lista_cnpj['Titular']}\nSaldo: {lista_cnpj['Saldo']}\nLimite: {lista_cnpj['Limite']}")
                else:
                    sleep(0.5)
                    print(f"\033[31mNúmero de conta {termo} inexistente\33[m")

        elif opcao == 0:
            print("\033[32mSaindo da opção de Extrato\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 0 e 3\33[m")
    print("\033[36m-\33[m" *85)
    os.system('pause')


# Função principal que executa todo o processo
def menu():
    os.system('cls')
    while True:
        titulo("BEM-VINDO AO SISTEMA DE BANCO 24HRs".center(85))
        print("1 - Abrir Conta\n2 - Consultar Conta\n3 - Sacar\n4 - Depositar\n5 - Extrato\n0 - Sair")
        print("\033[36m-\33[m" *85)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            consultar_conta()
        elif opcao == 3:
            sacar_conta()
        elif opcao == 4:
            depositar()
        elif opcao == 5:
            extrato()
        elif opcao == 0:
            sleep(0.5)
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 0 e 3\33[m")

menu()
