import os # Manipulação de caminhos de diretórios.
import re
import sqlite3 # Conexão com o banco de dados SQLite
import logging # Criação de registros de eventos para o seu programa.
import requests # Permite fazer solicitações HTTP para baixar arquivos da internet
import pandas as pd
from pathlib import Path # Manipular caminhos de arquivos e diretórios.
from bs4 import BeautifulSoup

# -----------------------------------------------------------------------------------------------------------
# 1. Criar diretório de destino
# 2. Extrair dados da página HTML:
# 3. Criar diretório do banco de dados
# 4. Salvar o arquivo excel no diretório destino
# 5. Criar a tabela
# 6. Inserir registros na tabela
# 7. Popular os dados no banco de dados SQLite

# -----------------------------------------------------------------------------------------------------------
def criar_diretorio(folder):

    try:
        diretorio = Path(__file__).resolve().parent / f'datalake/bronze/{folder}'
        diretorio.mkdir(parents=True, exist_ok=True)
        logging.info('Diretório criado com sucesso.')
        return diretorio
    except Exception as e:
        logging.error(f'Falha ao criar diretorio: {e}')
        return None

# -----------------------------------------------------------------------------------------------------------
def extrair_dados(base_url):

    """
    Extrai SIGLAS de uma página HTML.

    Args:
        base_url (str): URL da página da qual extrair os dados posição, jogos, vitorias, empates e derrotas.

    Returns:
        dict: Dicionário que contém os dados extraídos.

    """

    tabela_dict = {"posicao":[], "nome_time":[], "total_pontos":[], "jogos":[],
                   "vitorias":[], "empates":[], "derrotas":[]}

    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            tabela = soup.find('table', class_='table m-b-20 tabela-expandir')
            if tabela:
                linhas = tabela.find_all('tr', class_='expand-trigger')
                for linha in linhas:
                    # Extrair o nome do time
                    times = linha.find('span', class_='hidden-xs')
                    if times:
                        nome_time = times.text.strip()
                    # Extrair os pontos
                    pontos = linha.find('th', scope='row')
                    if pontos:
                        total_pontos = pontos.text.strip()
                    
                    # Extrair os dados de posição, jogos, vitorias, empates e derrotas
                    dados = linha.find_all('td')
                    posicao = re.findall(r'\d+', dados[0].text.strip())[0]
                    jogos = re.findall(r'\d+', dados[1].text.strip())[0]
                    vitorias = re.findall(r'\d+', dados[2].text.strip())[0]
                    empates = re.findall(r'\d+', dados[3].text.strip())[0]
                    derrotas = re.findall(r'\d+', dados[4].text.strip())[0]

                    tabela_dict["posicao"].append(posicao)
                    tabela_dict["nome_time"].append(nome_time)
                    tabela_dict["total_pontos"].append(total_pontos)
                    tabela_dict["jogos"].append(jogos)
                    tabela_dict["vitorias"].append(vitorias)
                    tabela_dict["empates"].append(empates)
                    tabela_dict["derrotas"].append(derrotas)               
        else:
            logging.info(f'Solicitação falhou. Código de status: {response.status_code}')
    except Exception as e:
        logging.error(f'Erro ao fazer a extrair dados: {e}')

    return tabela_dict

# -----------------------------------------------------------------------------------------------------------
def salvar_excel(tabela_dict, diretorio_destino):

    """
    Salva os dados de uma tabela em formato de dicionário em um arquivo Excel.

    Args:
    tabela_dict: dict
        Um dicionário contendo os dados da tabela a serem salvos. As chaves devem ser os nomes das colunas e os valores devem ser listas com os valores das células.
    diretorio_destino : str
        O diretório onde o arquivo Excel será salvo.

    Returns:
    pandas.DataFrame or None
        Um DataFrame pandas contendo os dados da tabela, ou None se ocorrer um erro durante o processo de salvamento.

    """

    try:
        df = pd.DataFrame(tabela_dict, columns=["posicao", "nome_time", "total_pontos", "jogos", "vitorias", "empates", "derrotas"])
        df.to_excel(diretorio_destino / "tabela_brasileirao_2024.xlsx", index=False)
        return df
    except Exception as e:
        logging.error(f'Erro ao fazer a criar a tabela: {e}')
        return None

# -----------------------------------------------------------------------------------------------------------
def diretorio_db(database):

    """
    Estabelece uma conexão com o banco de dados SQLite.

    Args:
        database (str): Nome do diretório onde o banco de dados será criado.

    Returns:
        str: Caminho completo do banco de dados SQLite.
    """

    try:
        base_path = os.path.dirname(__file__)
        base_folder = os.path.join(base_path + f'/cadastro/{database}.db').replace('\\', '/')
        os.makedirs(base_folder)
        print(f'{base_folder} database criado com sucesso.')
    except FileExistsError:
        print(f'{base_folder} database já existe.')

    return base_folder

# -----------------------------------------------------------------------------------------------------------
def criar_tabela(cursor):

    """
    Cria uma tabela no banco de dados SQLite para armazenar dados da tabela do Campeonato Brasileiro.

    Args:
    cursor : sqlite3.Cursor
        Um cursor SQLite para executar comandos SQL no banco de dados.

    Returns:
    None

    Except:
    sqlite3.Error
        Se ocorrer um erro ao executar o comando SQL para criar a tabela.

    Example:
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    criar_tabela(cursor)
    conn.close()
    """

    try:
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tb_tabela_brasileirao(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        posicao INTEGER,
                        nome_time TEXT,
                        total_pontos INTEGER,
                        jogos INTEGER,
                        vitorias INTEGER,
                        empates INTEGER,
                        derrotas INTEGER
                        )""")
        
        print('Tabela criada com sucesso.')

    except sqlite3.Error as e:
        logging.error(f'Erro ao criar a tabela: {e}')

# -----------------------------------------------------------------------------------------------------------
def inserir_registros(cursor, conn, df_tabela):

    """
    Insere registros em uma tabela do banco de dados SQLite com base em um DataFrame pandas.

    Args:
    cursor : sqlite3.Cursor
        Um cursor SQLite para executar comandos SQL no banco de dados.
    conn : sqlite3.Connection
        Uma conexão SQLite para o banco de dados.
    df_tabela : pandas.DataFrame
        Um DataFrame pandas contendo os registros a serem inseridos na tabela.

    Returns:
    None

    Except:
    sqlite3.Error
        Se ocorrer um erro ao executar o comando SQL para inserir os registros na tabela.

    Example:
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    inserir_registros(cursor, conn, df_tabela)
    conn.close()
    """

    try:
        for index, row in df_tabela.iterrows():
            cursor.execute("""
                        INSERT INTO tb_tabela_brasileirao(
                            posicao, nome_time, total_pontos, jogos, vitorias, empates, derrotas)
                        VALUES (?, ?, ?, ?, ?, ?, ?)""",
                        (row['posicao'], row['nome_time'], row['total_pontos'], row['jogos'], row['vitorias'], row['empates'], row['derrotas']))
            conn.commit()
            print('Dados inseridos na tabela com sucesso.')

    except sqlite3.Error as e:
        logging.error(f'Erro ao inserir dados na tabela: {e}')      

# -----------------------------------------------------------------------------------------------------------
def main():

    folder = 'tabela_brasileirao_2024'
    base_url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2024'
    diretorio_destino = criar_diretorio(folder)
    if diretorio_destino:
        print(f'Diretório Destino: {diretorio_destino}')
        tabela_dict = extrair_dados(base_url)
        if tabela_dict:
            df_tabela = salvar_excel(tabela_dict, diretorio_destino)
            if df_tabela is not None:
                print(df_tabela)
    else:
        print('Falha ao criar o diretório de destino. Verifique o log para mais detalhes.')
    
    # Conectar ao banco de dados SQLite
    database = 'cadastro'
    path_db = diretorio_db(database)
    if path_db:
        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        criar_tabela(cursor)
        if df_tabela is not None:
            inserir_registros(cursor, conn, df_tabela)
        else:
            logging.error('Não foi possível ler o arquivo Excel.')
    else:
        logging.error('Não foi possível criar o diretório do banco de dados.')

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()