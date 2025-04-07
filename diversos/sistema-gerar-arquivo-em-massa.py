import os
from time import sleep

# Lista com formato de arquivos
lista_formato = ["xlsx", "csv", "txt", "json", "sql", "db"]


# Função para criar linha e texto
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


# Função com entrada de número inteiro e interrupção do teclado
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


# def iteracao():
#         quantos_arquivos = int(input("• Quantos arquivos deseja gerar? "))
#         for c in range(0, quantos_arquivos):
#             try:
#                 with open(f"novo_arquivo_{c+1}.{lista_formato[0]}", "wt+") as arquivo:
#                     arquivo.close()
#             except:
#                 sleep(0.5)
#                 print("\033[31mErro na criação do arquivo\33[m")
#             else:
#                 sleep(0.5)
#                 print("\033[32mArquivo criado com sucesso\33[m")


# Função para criar arquivos com o tipo de formato selecionado
def criar_arquivo():
    os.system("cls")
    while True:
        titulo("FORMATO DE ARQUIVO".center(50))
        print("1 - XLSX\n2 - CSV\n3 - TXT\n4 - JSON\n5 - SQL\n6 - DB\n7 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a opção do arquivo: ")
        if opcao == 1:
            nome_arquivo = input("Digite o nome do arquivo: ")
            quantos_arquivos = int(input("• Quantos arquivos deseja gerar? "))
            for c in range(0, quantos_arquivos):
                try:
                    sleep(0.5)
                    with open(f"{nome_arquivo}_{c+1}.{lista_formato[0]}", "wt+") as arquivo:
                        arquivo.close()
                except:
                    sleep(0.5)
                    print("\033[31mErro na criação do arquivo\33[m")
                else:
                    sleep(0.5)
                    print("\033[32mArquivo criado com sucesso\33[m")
       
        elif opcao == 2:
            nome_arquivo = input("Digite o nome do arquivo: ")
            quantos_arquivos = int(input("• Quantos arquivos deseja gerar? "))
            for c in range(0, quantos_arquivos):
                try:
                    sleep(0.5)
                    with open(f"{nome_arquivo}_{c+1}.{lista_formato[1]}", "wt+") as arquivo:
                        arquivo.close()
                except:
                    sleep(0.5)
                    print("\033[31mErro na criação do arquivo\33[m")
                else:
                    sleep(0.5)
                    print("\033[32mArquivo criado com sucesso\33[m")
        
        elif opcao == 3:
            nome_arquivo = input("Digite o nome do arquivo: ")
            quantos_arquivos = int(input("• Quantos arquivos deseja gerar? "))
            for c in range(0, quantos_arquivos):
                try:
                    sleep(0.5)
                    with open(f"{nome_arquivo}_{c+1}.{lista_formato[2]}", "wt+") as arquivo:
                        arquivo.close()
                except:
                    sleep(0.5)
                    print("\033[31mErro na criação do arquivo\33[m")
                else:
                    sleep(0.5)
                    print("\033[32mArquivo criado com sucesso\33[m")
       
        elif opcao == 4:
            quantos_arquivos = int(input("• Quantos arquivos deseja gerar? "))
            for c in range(0, quantos_arquivos):
                try:
                    sleep(0.5)
                    with open(f"{nome_arquivo}_{c+1}.{lista_formato[3]}", "wt+") as arquivo:
                        arquivo.close()
                except:
                    sleep(0.5)
                    print("\033[31mErro na criação do arquivo\33[m")
                else:
                    sleep(0.5)
                    print("\033[32mArquivo criado com sucesso\33[m")
        
        elif opcao == 5:
            nome_arquivo = input("Digite o nome do arquivo: ")
            quantos_arquivos = int(input("• Quantos arquivos deseja gerar? "))
            for c in range(0, quantos_arquivos):
                try:
                    sleep(0.5)
                    with open(f"{nome_arquivo}_{c+1}.{lista_formato[4]}", "wt+") as arquivo:
                        arquivo.close()
                except:
                    sleep(0.5)
                    print("\033[31mErro na criação do arquivo\33[m")
                else:
                    sleep(0.5)
                    print("\033[32mArquivo criado com sucesso\33[m")
       
        elif opcao == 6:
            nome_arquivo = input("Digite o nome do arquivo: ")
            quantos_arquivos = int(input("• Quantos arquivos deseja gerar? "))
            for c in range(0, quantos_arquivos):
                try:
                    sleep(0.5)
                    with open(f"{nome_arquivo}_{c+1}.{lista_formato[5]}", "wt+") as arquivo:
                        arquivo.close()
                except:
                    sleep(0.5)
                    print("\033[31mErro na criação do arquivo\33[m")
                else:
                    sleep(0.5)
                    print("\033[32mArquivo criado com sucesso\33[m")
                    
        elif opcao == 7:
            sleep(0.5)
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")


# Função que executa todo o processo
def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA PARA CRIAR ARQUIVOS EM MASSA".center(50))
        print("1 - Formato de Arquivo\n2 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            criar_arquivo()
        elif opcao == 2:
            sleep(0.5)
            print("\033[32mSaindo do Programa... Até logo!\33[m")
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 1 e 2\33[m")

menu()
