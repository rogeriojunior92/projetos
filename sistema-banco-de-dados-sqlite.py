import os
import sqlite3
from sqlite3 import Error
from time import sleep

lista_tabela = []

#banco_dados = input("Crie um novo banco de dados: ")
#criar_tabela = input("Criar nova tabela: ")

# Diretório onde o banco de dados está criado
path = "C:/Users/Dell/Documents/SQLite/agenda.db"


def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


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
    titulo("VALIDAR CONEXÃO COM O BANCO DE DADOS".center(50))
    try:
        # Verifica no diretório se o banco de dados já existe
        if not (os.path.exists(path)):
            conn = sqlite3.connect(path)
            print("Banco criado com sucesso!")
    except Error as er:
        sleep(0.5)
        print(f"\033[31mOcorreu um erro na conexão ao banco de dados {er}\33[m")
    else:
        conn = sqlite3.connect(path)
        sleep(0.5)
        print("\033[31mO banco já existe, por isso não pode ser criado!\33[m")
        print("\033[32mConexão - OK\33[m")
    os.system("pause")
    return conn


# Função para criar tabela
def criar_tabela():
    os.system("cls")
    titulo("CRIAR TABELA NO BANCO DE DADOS".center(50))
    try:
        # Definindo o cursor (conexão ao banco)
        cursor = sqlite3.connect(path)
        # Criando a tabela
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS tb_contatos
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME VARCHAR(30) NOT NULL,
                SOBRENOME VARCHAR(30) NOT NULL,
                SEXO CHAR(1) NOT NULL,
                CPF INT,
                TELEFONE INT,
                EMAIL VARCHR(50) NOT NULL
            );"""
        )
        print("\033[32mTabela criada com sucesso\33[m")
    except Error as er:
        print(f"\033[31mOcorreu um erro na criação da tabela {er}\33[m")


# Função para listar tabelas de um banco
def listar_tabela():
    os.system("cls")
    titulo("LISTAR TABELAS NO BANCO DE DADOS".center(50))
    try:
        # Definindo a conexão ao banco
        conn = sqlite3.connect(path)
        # Consulta / listando tabelas existentes no banco
        sql_query = (
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table';
            """)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        
        print("ID".center(3), end='')
        print("Tabela".center(30))

        for indice_query in list(enumerate(cursor.fetchall(), start=1)):

            indice = indice_query[0]
            tabela = indice_query[1]

            print(str(indice).center(3), end='')
            print(str(tabela[0]).center(30))
        
    except Error as er:
        print(f"\033[31mOcorreu um erro na execução da query {er}\33[m")


def deletar_tabela():
    os.system("cls")
    titulo("DELETAR TABELA DO BANCO DE DADOS")
    termo = input("Informe o nome da tabela que deseja remover: ")
    conn = sqlite3.connect(path)
    try:
        sql_query = (
            f"""
            DROP TABLE tb_{termo}

        """)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        print("\033[32mTabela excluido com sucesso\33[m")
    except Error as er:
        print(f"\033[31mOcorreu um erro na exclusão da tabela {er}\33[m")


# Função para registrar dados no banco
def novo_registro():
    os.system("cls")
    titulo("NOVO REGISTRO".center(50))
    # Definindo a conexão ao banco
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    while True:
        sexo = input("Sexo: [M/F] ").upper()[0]
        if sexo in "MF":
            break
        print("\033[31mERRO! Digite apenas M ou F\33[m")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    
    cursor.execute(f"""
    INSERT INTO tb_contatos ('NOME', 'SOBRENOME', 'SEXO', 'CPF', 'TELEFONE', 'EMAIL')
    VALUES ('{nome}','{sobrenome}','{sexo}','{cpf}','{telefone}','{email}')""" 
    )
    conn.commit()
    sleep(0.5)
    print("\033[32mCadastrado com sucesso\33[m")
    os.system("pause")


def imprimir_registro():
    os.system("cls")
    titulo("IMPRIMIR REGISTRO".center(50))
    conn = sqlite3.connect(path)
    sql_query = ("""
    SELECT *
    FROM tb_contatos
    """)
    cursor = conn.cursor()
    cursor.execute(sql_query)

    print("ID".center(3), end='')
    print("NOME".center(20), end='')
    print("SOBRENOME".center(20), end='')
    print("SEXO".center(20), end='')
    print("CPF".center(20), end='')
    print("TELEFONE".center(20), end='')
    print("EMAIL".center(20))

    for indice_query in list(enumerate(cursor.fetchall(), start=1)):

        indice = indice_query[0]
        tabela = indice_query[1]
        
        print(str(indice).center(3), end='')
        print(str(tabela[1]).center(20), end='')
        print(str(tabela[2]).center(20), end='')
        print(str(tabela[3]).center(20), end='')
        print(str(tabela[4]).center(20), end='')
        print(str(tabela[5]).center(20), end='')
        print(str(tabela[6]).center(20))
        
    os.system("pause")


def buscar_registro():
    os.system("cls")
    titulo("BUSCAR REGISTRO".center(50))
    termo = input("Informe o nº CPF para buscar o registro: ")
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(
       f"""
        SELECT *
        FROM tb_contatos
        WHERE CPF = '{termo}'
    """)
    for agenda_cpf in cursor.fetchall():
        print(f"Nome: {agenda_cpf[1]}\nSobrenome: {agenda_cpf[2]}\nSexo: {agenda_cpf[3]}\nCPF: {agenda_cpf[4]}\nTelefone: {agenda_cpf[5]}\nE-mail: {agenda_cpf[6]}")
    conn.commit()
    os.system("pause")


def deletar_registro():
    os.system("cls")
    titulo("DELETAR REGISTRO".center(50))
    termo = input("Informe o nº CPF para deletar o registro: ")
    os.system("pause")


def atualizar_registro():
    os.system("cls")
    titulo("ATUALIZAR REGISTRO".center(50))
    termo = input("Informe o nº CPF para atualizar o registro: ")
    os.system("pause")


def menu():
    while True:
        titulo("SISTEMA BANCO DE DADOS - AGENDA ".center(50))
        print("1 - Conexão Banco de Dados\n2 - Criar Tabela\n3 - Listar Tabelas\n4 - Deletar Tabela\n5 - Novo Registro\n6 - Imprimir Registro\n7 - Buscar Registro\n8 - Deletar Registro\n9 - Atualizar Registro\n10 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            conexao_banco()
        elif opcao == 2:
            criar_tabela()
        elif opcao == 3:
            listar_tabela()
        elif opcao == 4:
            deletar_tabela()
        elif opcao == 5:
            novo_registro()
        elif opcao == 6:
            imprimir_registro()
        elif opcao == 7:
            buscar_registro()
        elif opcao == 8:
            deletar_registro()
        elif opcao == 9:
            atualizar_registro()
        elif opcao == 10:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 7\33[m")

menu()