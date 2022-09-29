# Imports as bibliotecas
import os
import sqlite3
import pandas as pd
from sqlite3 import Error
from faker import Faker
from time import sleep

# Lista para armazenar os dados Faker
lista_relatorio = []

# cursor: É um interador que permite navegar e manipular os registros do banco.
# execute: Lê e executa comandos SQL puro diretamente no banco.
# sqlite3.connect(): Para criar uma conexão com o banco de dados.
# cursor = conn.cursor(): Para executar instruções SQL e buscar resultados de consultas SQL, precisaremos usar um cursor de banco de dados.
# commit(): É ele que grava de fato as alterações na tabela. Lembrando que uma tabela é alterada com as instruções SQL: INSERT, UPDATE e DELETE.

# Variavéis para converter os dados PT-BR
locale = 'pt-BR'
fake = Faker(locale)


# Diretório onde o banco de dados está criado
path = "C:\\Users\\Dell\\Documents\\SQLite\\dados_faker.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()


# Função para criar linha e título
def titulo(txt):
    print("\033[36m-\033[m" *50)
    print("\033[36m"+txt+"\033[m")
    print("\033[36m-\033[m" *50)


# Função para validar número inteiro e interrupção pelo teclado (ENTER)
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


# Função para criar conexão com o Banco de Dados
def conexao_banco():
    os.system("cls")
    try:
        # Verifica no diretório se o banco de dados já existe
        if not(os.path.exists(path)):
            # Conexão sqlite3 com banco de dados
            conn = sqlite3.connect(path)
            print("\033[32mBanco criado com sucesso!\33[m")
    except Error as er:
        print(f"\033[31mOcorreu um erro na conexão ao banco de dados. {er}\33[m")
    else:
        conn = sqlite3.connect(path)
        print("\033[31mO banco já existe, por isso não pode ser criado.\33[m")
        sleep(0.5)
        print("Conexão - OK")
    os.system("pause")
    return conn
    

# Função para criar tabela
def criar_tabela():
    os.system("cls")
    termo = input("\033[1;90m• Favor, digite o nome da tabela que deseja criar: \033[0;0m")
    try:
        tables = ("""
        CREATE TABLE IF NOT EXISTS tb_dados_faker
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME VARCHAR(50) NOT NULL,
            CIDADE VARCHAR(30) NOT NULL,
            ESTADO VARCHAR(30) NOT NULL,
            TELEFONE VARCHAR(30) NOT NULL,
            EMAIL VARCHAR(30) NOT NULL,
            TRABALHO VARCHAR(30) NOT NULL
        );"""
    )
        cursor.execute(tables)
        sleep(0.5)
        print(f"Tabela \033[32mtb_{termo}\33[m criada com sucesso.")
    except Error as er:
        sleep(0.5)
        print(f"\033[31mOcorreu um erro na criação da tabela {er}\33[m")
    os.system("pause")


# Função para gerar dados fakes
def gerar_dados_faker():
    os.system("cls")
    try:
        # Laço de repetição para determinar quantos dados serão gerados
        for c in range(100):
            nome = fake.name()
            cidade = fake.city()
            estado = fake.state()
            telefone = fake.phone_number()
            email = fake.email()
            trabalho = fake.job()

            lista_relatorio.append((nome, cidade, estado, telefone, email, trabalho))
            #print(lista_relatorio)

            cursor.execute(f"""
                INSERT INTO tb_dados_faker ("NOME", "CIDADE", "ESTADO", "TELEFONE", "EMAIL", "TRABALHO")
                VALUES ('{nome}', '{cidade}', '{estado}', '{telefone}', '{email}', '{trabalho}')""")
            # Grava as alterações na tabela com as instruções SQL: INSERT, UPDATE e DELETE.
            conn.commit()
        print("\033[32mDados Faker gerado com sucesso\33[m")
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na criação dos Dados Fakes\33[m")
    os.system("pause")


# Função para gerar relatório Excel
def gerar_relatorio():
    os.system("cls")
    relatorios = int(input("\033[1;90mDeseja gerar quantos relatórios Excel? \033[0;0m"))
    for c in range(0, relatorios):
        try:
            df = pd.DataFrame(lista_relatorio, columns=["NOME", "CIDADE", "ESTADO", "TELEFONE", "EMAIL", "TRABALHO"])
            df.to_excel(f"dados_faker_{c+1}.xlsx", index=False)
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
        titulo("SISTEMA - GERADOR DADOS FAKER SQLITE".center(50))
        print("1 - Conexão Banco de Dados\n2 - Criar Tabela\n3 - Gerar Dados Faker\n4 - Gerar Relatório\n0 - Sair")
        print("\033[36m-\033[m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            conexao_banco()
        elif opcao == 2:
            criar_tabela()
        elif opcao == 3:
            gerar_dados_faker()
        elif opcao == 4:
            gerar_relatorio()
        elif opcao == 0:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 0 e 3\33[m")

menu()
