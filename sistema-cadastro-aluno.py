from datetime import datetime
import os
from time import sleep

nome_escola = "FACULDADE VIRTUAL PYTHON"
separador = "-" * len(nome_escola)
cabecalho = f"{separador}\n{nome_escola}\n{separador}\n"


# Função para criar título e linha
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


# Funçãio que válida número inteiro e interrupção do teclado
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


# Função para criar um arquivo novo formato .TXT
def novo_arquivo():
    os.system("cls")
    try:
        arquivo = open("cadastro_aluno.txt", "wt+", encoding="utf-8")
        arquivo.write(cabecalho)
        arquivo.close()
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na criação do arquivo\33[m")
    else:
        sleep(0.5)
        print("\033[32mArquivo criado com sucesso\33[m")
    os.system("pause")


# Função para salvar o cadastro do aluno(a)
def salvar_cadastro(aluno):
    try:
        arquivo = open("cadastro_aluno.txt", "r", encoding="utf-8")
        indice_aluno = arquivo.read().count("Aluno") + 1
        arquivo.close()
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na escrita do arquivo\33[m")
    else:
        try:
            data = datetime.now()
            data_atual = data.strftime('%d/%m/%Y - %H:%M')
            arquivo = open("cadastro_aluno.txt", "a+t", encoding="utf-8")
            arquivo.write(f"\nAluno {indice_aluno}\nRegistro: {data_atual}\n")
        except:
            sleep(0.5)
            print("\033[31mOcorreu um erro na gravação do arquivo\33[m")
        else:
            sleep(0.5)
            print("\033[32mAluno(a) cadastrado com sucesso!\33[m")
    
    for chave in aluno:
        arquivo.write(f"{chave}: {aluno[chave]}\n")


# Função para cadastrar um novo aluno(a)
def cadastrar_aluno():
    os.system("cls")
    aluno = {
        "Nome": "",
        "CPF": "",
        "Data de Nascimento": "",
        "Idade": 0,
        "Serie": ""
    }

    print("Favor, digite os campos abaixo para cadastrar um novo aluno: ")
    for chave in aluno:
        aluno[chave] = input(f"{chave}: ")

    salvar_cadastro(aluno)
    os.system("pause")


# Função principal que executa todo processo
def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA CADASTRO DE ALUNOS".center(50))
        print("1 - Novo Arquivo\n2 - Cadastrar Aluno(a)\n3 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            novo_arquivo()
        elif opcao == 2:
            cadastrar_aluno()
        elif opcao == 3:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 3\33[m")

menu()
