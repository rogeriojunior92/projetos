import os
import sqlite3
from sqlite3 import Error
from time import sleep

# cursor: É um interador que permite navegar e manipular os registros do banco.
# execute: Lê e executa comandos SQL puro diretamente no banco.
# sqlite3.connect(): Para criar uma conexão com o banco de dados.
# cursor = conn.cursor(): Para executar instruções SQL e buscar resultados de consultas SQL, precisaremos usar um cursor de banco de dados.
# commit(): É ele que grava de fato as alterações na tabela. Lembrando que uma tabela é alterada com as instruções SQL: INSERT, UPDATE e DELETE.
# fetchall(): Para buscar todos os registros no banco.

# Diretório onde o banco de dados está criado
path = "C:/Users/Dell/Documents/SQLite/agenda.db"


# Função para criar linha e título
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *60)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *60)


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
    titulo("CONEXÃO COM O BANCO DE DADOS".center(60))
    try:
        # Verifica no diretório se o banco de dados já existe
        if not (os.path.exists(path)):
            # Conexão sqlite3 com banco de dados
            conn = sqlite3.connect(path)
            sleep(0.5)
            print("\033[32mBanco criado com sucesso!\33[m")
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
    titulo("CRIAR TABELA NO BANCO DE DADOS".center(60))
    try:
        # Conexão sqlite3 com banco de dados
        cursor = sqlite3.connect(path)
        # Criar tabela
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
        sleep(0.5)
        print("\033[32mTabela criada com sucesso\33[m")
    except Error as er:
        sleep(0.5)
        print(f"\033[31mOcorreu um erro na criação da tabela {er}\33[m")


# Função para listar tabelas existentes no banco
def listar_tabela():
    os.system("cls")
    titulo("LISTAR TABELAS NO BANCO DE DADOS".center(60))
    try:
        # Conexão sqlite3 com banco de dados
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
        sleep(0.5)
        print(f"\033[31mOcorreu um erro na execução da query {er}\33[m")
    os.system("pause")


# Função para deletar tabela
def deletar_tabela():
    os.system("cls")
    titulo("DELETAR TABELA DO BANCO DE DADOS".center(60))
    termo = input("Informe o nome da tabela que deseja remover: ")
    # Conexão sqlite3 com banco de dados
    conn = sqlite3.connect(path)
    try:
        sql_query = (f"""DROP TABLE tb_{termo}""")
        cursor = conn.cursor()
        cursor.execute(sql_query)
        sleep(0.5)
        print(f"Tabela \033[32mtb_{termo}\33[m excluido com sucesso")
    except Error as er:
        sleep(0.5)
        print(f"\033[31mOcorreu um erro na exclusão da tabela {er}\33[m")
    os.system("pause")


# Função para registrar dados no banco
def novo_registro():
    os.system("cls")
    titulo("INSERIR NOVO REGISTRO NO BANCO DE DADOS".center(60))
    # Conexão sqlite3 com banco de dados
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    print("• Favor, preencher os campos abaixo para cadastro: ")
    nome = input("\033[1;90mNome: \033[0;0m")
    sobrenome = input("\033[1;90mSobrenome: \033[0;0m")
    while True:
        sexo = input("\033[1;90mSexo: [M/F] \033[0;0m").upper()[0]
        if sexo in "MF":
            break
        print("\033[31mERRO! Digite apenas M ou F\33[m")
    cpf = input("\033[1;90mCPF: \033[0;0m")
    telefone = input("\033[1;90mTelefone: \033[0;0m")
    email = input("\033[1;90mE-mail: \033[0;0m")
    
    cursor.execute(f"""
    INSERT INTO tb_contatos ('NOME', 'SOBRENOME', 'SEXO', 'CPF', 'TELEFONE', 'EMAIL')
    VALUES ('{nome}','{sobrenome}','{sexo}','{cpf}','{telefone}','{email}')""")
    conn.commit()

    sleep(0.5)
    print("\033[32mCadastrado com sucesso\33[m")
    os.system("pause")


# Função para imprimir / listar os dados da tabela
def imprimir_registro():
    os.system("cls")
    titulo("LISTAR CADASTROS DO BANCO DE DADOS".center(60))
    # Conexão sqlite3 com banco de dados
    conn = sqlite3.connect(path)
    sql_query = (
        """SELECT *
        FROM tb_contatos""")
    cursor = conn.cursor()
    cursor.execute(sql_query)

    print("ID".center(3), end='')
    print("NOME".center(20), end='')
    print("SOBRENOME".center(20), end='')
    print("SEXO".center(10), end='')
    print("CPF".center(20), end='')
    print("TELEFONE".center(20), end='')
    print("EMAIL".center(20))

    for indice_query in list(enumerate(cursor.fetchall(), start=1)):

        indice = indice_query[0]
        tabela = indice_query[1]
        
        print(str(indice).center(3), end='')
        print(str(tabela[1]).center(20), end='')
        print(str(tabela[2]).center(20), end='')
        print(str(tabela[3]).center(10), end='')
        print(str(tabela[4]).center(20), end='')
        print(str(tabela[5]).center(20), end='')
        print(str(tabela[6]).center(20))        
    os.system("pause")


# Função para buscar registro no banco
def buscar_registro():
    os.system("cls")
    titulo("BUSCAR REGISTROS NO BANCO DE DADOS".center(60))
    termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
    # Conexão sqlite3 com banco de dados
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(
       f"""
        SELECT *
        FROM tb_contatos
        WHERE CPF = '{termo}'""")

    for agenda_cpf in cursor.fetchall():
        sleep(0.5)
        print(f"Nome: {agenda_cpf[1]}\nSobrenome: {agenda_cpf[2]}\nSexo: {agenda_cpf[3]}\nCPF: {agenda_cpf[4]}\nTelefone: {agenda_cpf[5]}\nE-mail: {agenda_cpf[6]}")
    print("\033[1;94m-\033[0;0m" *60)
    conn.commit()
    os.system("pause")


# Função para deletar registro no banco 
def deletar_registro():
    os.system("cls")
    titulo("DELETAR REGISTRO NO BANCO DE DADOS".center(60))
    termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
    # Conexão sqlite3 com banco de dados
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(
        f"""
        DELETE
        FROM tb_contatos 
        WHERE CPF = '{termo}'
        """)
    conn.commit()
    print(f"CPF {termo} deletado com sucesso")
    os.system("pause")


def atualizar_registro():
    os.system("cls")
    titulo("ATUALIZAR REGISTRO NO BANCO DE DADOS".center(60))
    buscar_registro()
    # Conexão sqlite3 com banco de dados
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    while True:
        print("\033[1;90mCampos para alteração\033[0;0m")
        print("\033[1;90m1 - Nome\n2 - Sobrenome\n3 - Sexo\n4 - CPF\n5 - Telefone\n6 - Email\n7 - Sair\033[0;0m")
        print("\033[1;94m-\033[0;0m" *60)
        
        opcao = leiaInt("Digite a sua opção para alterar o cadastro: ")
        if opcao == 1:
            termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
            alterar_nome = input("\033[1;90mAlterar nome para: \033[0;0m")
            cursor.execute(f"""
                UPDATE tb_contatos
                SET NOME = '{alterar_nome}'
                WHERE CPF = '{termo}'
                """)
            conn.commit()
            sleep(0.5)
            print("\033[32mRegistro atualizado com sucesso\33[m")

        elif opcao == 2:
            termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
            alterar_sobrenome = input("\033[1;90mAlterar sobrenome para: \033[0;0m")
            cursor.execute(f"""
                UPDATE tb_contatos
                SET SOBRENOME = '{alterar_sobrenome}'
                WHERE CPF = '{termo}'
                """)
            conn.commit()
            sleep(0.5)
            print("\033[32mRegistro atualizado com sucesso\33[m")

        elif opcao == 3:
            termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
            while True:
                alterar_sexo = input("\033[1;90mAlterar sexo para: [M/F] \033[0;0m").upper()[0]
                if alterar_sexo in "MF":
                    break
                print("ERRO! Digite apenas M ou F")
                cursor.execute(f"""
                    UPDATE tb_contatos
                    SET SEXO = '{alterar_sexo}'
                    WHERE CPF = '{termo}'
                    """)
            conn.commit()
            sleep(0.5)
            print("\033[32mRegistro atualizado com sucesso\33[m")

        elif opcao == 4:
            termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
            alterar_cpf = input("\033[1;90mAlterar CPF para: \033[0;0m")
            cursor.execute(f"""
                UPDATE tb_contatos
                SET CPF = '{alterar_cpf}'
                WHERE CPF = '{termo}'
                """)
            conn.commit()
            sleep(0.5)
            print("\033[32mRegistro atualizado com sucesso\33[m")

        elif opcao == 5:
            termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
            alterar_telefone= input("\033[1;90mAlterar telefone para: \033[0;0m")
            cursor.execute(f"""
                UPDATE tb_contatos
                SET TELEFONE = '{alterar_telefone}'
                WHERE CPF = '{termo}'
                """)
            conn.commit()
            sleep(0.5)
            print("\033[32mRegistro atualizado com sucesso\33[m")

        elif opcao == 6:
            termo = input("\033[1;90m• Favor, innformar o nº CPF para buscar o registro: \033[0;0m")
            alterar_email = input("\033[1;90mAlterar e-mail para: \033[0;0m")
            cursor.execute(f"""
                UPDATE tb_contatos
                SET EMAIL = '{alterar_email}'
                WHERE CPF = '{termo}'
                """)
            conn.commit()
            sleep(0.5)
            print("\033[32mRegistro atualizado com sucesso\33[m")

        elif opcao == 7:
            sleep(0.5)
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 1 e 7\33[m")
    os.system("pause")


def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA BANCO DE DADOS".center(60))
        print("\033[1;90m1 - Conexão Banco de Dados\n2 - Criar Tabela\n3 - Listar Tabelas\n4 - Deletar Tabela\033[0;0m")
        titulo("CADASTRO BANCO DE DADOS".center(60))
        print("\033[1;90m5 - Novo Registro\n6 - Imprimir Registro\n7 - Buscar Registro\n8 - Deletar Registro\n9 - Atualizar Registro\n0 - Sair\033[0;0m")
        print("\033[1;94m-\033[0;0m" *60)

        opcao = leiaInt("\033[1;90mDigite a sua opção:\033[0;0m ")
        print("\033[1;94m-\033[0;0m" *60)
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
        elif opcao == 0:
            sleep(0.5)
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            sleep(0.5)
            print("\033[31mOpção inválida. Digite entre 0 e 9\33[m")

menu()
