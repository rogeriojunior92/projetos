import os
import pandas as pd
from time import sleep
from datetime import datetime
import win32com.client as win32

lista_agenda = []
limite_agenda = 15


def titulo(txt):
    print("\033[34m-\033[0;0m" *60)
    print('\033[34m'+txt+'\033[0;0m')
    print("\033[34m-\033[0;0m" *60)


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num

# Função para criar um arquivo .TXT
def novo_arquivo():
    os.system("cls")
    try:
        agenda = open("cadastro_agenda.txt", "wt+")
        agenda.close()
    except:
        sleep(0.5)
        print("\033[31mHouve um erro na criação do arquivo.\33[m")
    else:
        sleep(0.5)
        print("\033[32mArquivo criado com sucesso.\33[m")
    os.system("pause")


# Função para cadastrar
def novo_cadastro():
    os.system("cls")

    limite_cadastro_agenda = len((lista_agenda))
    if limite_cadastro_agenda < limite_agenda:

        titulo("\033[32m• Favor, preencher os campos abaixo para cadastrar um contato\33[m".center(60))
        try:
            data = datetime.now()
            data_atual = data.strftime('%d/%m/%Y - %H:%M')
            print(f"Data de registro: {data_atual}")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
        except:
            sleep(0.5)
            print("\033[31mHouve um erro no cadastro do contato.\33[m")
        else:
            sleep(0.5)
            print("\033[32mContato cadastrado com sucesso.\33[m")
        lista_agenda.append((nome, telefone, email))

        # Gravar dados no arquivo .TXT
        try:
            agenda = open("cadastro_agenda.txt", "at")
        except:
            sleep(0.5)
            print("\033[31mERRO! Arquivo na leitura do arquivo!\33[m")
        else:
            try:
                agenda.write(f"{lista_agenda}")
            except:
                sleep(0.5)
                print("\033[31mERRO! Na gravação do arquivo.\33[m")
            else:
                sleep(0.5)
                print("\033[32mContato cadastrado no arquivo com sucesso.\33[m")
    else:
        print(f"\033[31mERRO! Não é possível cadastrar mais contatos. Limite de {limite_agenda} atingido\33[m")
    os.system("pause")


# Função para imprimir / listar cadastro
def imprimir_cadastro():
    os.system("cls")
    titulo("\033[32mLISTA DE CONTATOS\33[m".center(60))
    print("ID".center(3), end='')
    print("Nome".center(20), end='')
    print("Telefone".center(20), end='')
    print("E-mail".center(20))

    # Criar os indices / posições na lista.
    for indice_agenda in list(enumerate(lista_agenda, start=1)):
        
        indice = indice_agenda[0]
        agenda = indice_agenda[1]

        print(str(indice).center(3), end='')
        print(str(agenda[0]).center(20), end='')
        print(str(agenda[1]).center(20), end='')
        print(str(agenda[2]).center(20))
    os.system("pause")


# Função para buscar contato pelo nome
def buscar_cadastro():
    os.system("cls")
    titulo("\033[32mBUSCAR CONTATO PELO O NOME INFORMADO\33[m".center(60))
    termo = input("• Informe o nome do contato: ")
    print("\033[34m-\033[0;0m" *60)
    for agenda in lista_agenda:
        nome, telefone, email = agenda
        if nome == termo:
            sleep(0.5)
            print(f"Nome: {nome}\nTelefone: {telefone}\nE-mail: {email}")
    print("\033[34m-\033[0;0m" *60)
    os.system("pause")


# Função para deletar contato pelo nome
def deletar_cadastro():
    os.system("cls")
    titulo("\033[32mDELETAR CONTATO PELO O NOME INFORMADO\33[m".center(60))
    termo = input("• Informe o nome do contato para deletar: ")
    for agenda in lista_agenda:
        nome, telefone, email = agenda
        if nome == termo:
            lista_agenda.remove((nome, telefone, email))
            sleep(0.5)
            print(f"• Contato {termo} excluído com sucesso.")
    print("\033[34m-\033[0;0m" *60)
    os.system("pause")


# Função que atualiza os dados
def atualizar_cadastro():
    os.system("cls")
    titulo("\033[32mATUALIZAR CONTATO PELO O NOME INFORMADO\33[m".center(60))
    pass
    os.system("pause")


def relatorio_excel():
    print("\033[32mGERANDO RELATÓRIO EXCEL...\33[m")
    sleep(1)
    try:
        df = pd.DataFrame(lista_agenda, columns=["Nome","Telefone","E-mail"])
        df.to_excel("lista_agenda.xlsx")
    except:
        sleep(0.5)
        print(f"\033[31mERRO! Não foi possível criar o relatório\33[m")
    else:
        sleep(0.5)
        print("\033[32mRelatório criado com sucesso.\33[m")


def enviar_email():
    os.system("cls")
    titulo("\033[32mENVIAR E-MAIL\33[m".center(60))
    print("Conectando ao servidor...")
    try:
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)
        email.To = "seu_email@email.com"
        email.Subject = "Cadastro de Agenda"
        email.HTMLBody = """
        <p>Olá,</p>
        
        <p>Segue a lista de agenda cadastrado.</p>  
        """
        anexo = "C:/Users/Dell/Documents/Eng/Projetos/lista_agenda.xlsx"
        email.Attachments.Add(anexo)
        email.Save()
        email.Send()
        print("\033[32mE-mail enviado com sucesso!\33[m")
    except Exception as erro:
        sleep(1)
        print(f"\033[31mERRO! Não foi possível enviar o e-mail!\33[m")
    os.system("pause")


# Função principal que executa todo o processo
def menu():
    while True:
        titulo("MENU - SISTEMA DE AGENDA".center(60))
        print("1 - NOVO ARQUIVO\n2 - CADASTRAR CONTATO\n3 - IMPRIMIR CONTATO\n4 - BUSCAR CONTATO\n5 - DELETAR CONTATO\n6 - ATUALIZAR CONTATO\n7 - CRIAR RELATÓRIO EXCEL\n8 - ENVIAR E-MAIL\n9 - SAIR")
        print("\033[34m-\033[0;0m" *60)
        print(f"Ao todo foram cadastrado(s): \033[32m{len(lista_agenda)}\33[m contato(s)")
        print("\033[34m-\033[0;0m" *60)

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
            relatorio_excel()
        elif opcao == 8:
            enviar_email()
        elif opcao == 9:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 8!\33[m")

menu()
