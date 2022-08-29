import requests
import os
import pandas as pd
from time import sleep

# Referência Via CEP - https://viacep.com.br/

# Função para criar título e linha
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


# Função para validar número inteiro e interrupção de teclado (usuário)
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


# Função para buscar informações do CEP
def buscar_informacoes_cep():
    os.system("cls")
    titulo("BUSCAR INFORMAÇÕES PELO CEP".center(50))
    cep = input("Digite o CEP: ")
    
    # Validar digitos, que seja igual 8
    if len(cep) == 8:
        link = f"https://viacep.com.br/ws/{cep}/json/"
        # Requisição do link
        requisicao = requests.get(link)
        print(requisicao)
        # Exibir as informações no formato JSON
        dic_resposta = requisicao.json()
        print(dic_resposta)

        sleep(0.5)
        print("\033[1;94m-\033[0;0m" *50)
        print(f"CEP: {dic_resposta['cep']}")
        print(f"Logradouro: {dic_resposta['logradouro']}")
        print(f"Complemento: {dic_resposta['complemento']}")
        print(f"Bairro: {dic_resposta['bairro']}")
        print(f"Localidade: {dic_resposta['localidade']}")
        print(f"UF: {dic_resposta['uf']}")

    else:
        print(f"CEP \033[31m{cep}\33[m INVÁLIDO")
    print("\033[1;94m-\033[0;0m" *50)
    
    os.system("pause")


# Função para buscar informações do CEP pelo endereço
def buscar_informacoes_endereco():
    os.system("cls")
    titulo("BUSCAR INFORMAÇÕES PELO ENDEREÇO".center(50))
    uf = input("Digite UF: ")
    cidade = input("Digite a cidade: ")
    endereco = input("Digite o endereço: ")
    link = f"https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/"
    
    requisacao = requests.get(link)
    print(requisacao)
    dic_requisicao = requisacao.json()
    print(dic_requisicao)
    
    
    # Gerar relatório em Excel
    try:
        df_endereco = pd.DataFrame(dic_requisicao, columns=["cep", "logradouro", "complemento", "bairro", "localidade", "uf", "ddd"])
        df_endereco.to_excel("relatorio_endereco.xlsx")
        print("\033[32mRelátório gerado com sucesso\33[m")
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na criação do relatório Excel\33[m")

    os.system("pause")


# Função principal que executa todo processo
def menu():
    os.system("cls")
    while True:
        titulo("API - CONSULTAR CEP".center(50))
        print("1 - Pesquisa de CEP pelo número\n2 - Pesquisa de CEP pelo endereço\n3 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            buscar_informacoes_cep()
        elif opcao == 2:
            buscar_informacoes_endereco()
        elif opcao == 3:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 3\33[m")


menu()
