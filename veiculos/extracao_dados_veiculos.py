# Importar bibliotecas
import os
import sqlite3
import logging
import requests
import pandas as pd
from pathlib import Path

# ---------------------------------------------------------------------------------------
def criar_diretorio_de_destino(pasta):

    """
    Cria um diretório para armazenar os arquivos baixados.

    Args:
        pasta (str): O nome da pasta a ser criada.

    Returns:
        Path: O caminho para o diretório criado.
    """

    try:
        diretorio = Path(__file__).resolve().parent / f'datalake/bronze/{pasta}'
        diretorio.mkdir(parents=True, exist_ok=True)
        logging.info('Diretório criado com sucesso.')
        return diretorio
    except Exception as e:
        logging.error(f'Falha ao criar diretório: {e}')


# ---------------------------------------------------------------------------------------
def baixar_arquivo_csv(base_url_cars, diretorio_destino):

    """
    Baixa um arquivo CSV a partir de uma URL e o salva no diretório de destino.

    Args:
        base_url_cars (str): A URL do arquivo CSV a ser baixado.
        diretorio_destino (Path): O caminho para o diretório onde o arquivo será salvo.

    Returns:
        bool: True se o download for bem-sucedido, False caso contrário.
    """

    try:
        response = requests.get(base_url_cars)
        if response.status_code == 200:
            with open(diretorio_destino / 'cars.csv', 'wb') as arquivo:
                arquivo.write(response.content)
                logging.info('Arquivo baixado e salvo com sucesso.')
                return True
        else:
            print(f'Falha ao baixar o arquivo. Status code: {response.status_code}')
            return False
    except Exception as e:
        logging.error(f'Erro ao baixar o arquivo: {e}')
        return False
    

# ---------------------------------------------------------------------------------------
def ler_arquivo_csv(diretorio_destino):

    """
    Lê um arquivo CSV a partir do diretório especificado.

    Args:
        diretorio_destino (Path): O caminho para o diretório onde o arquivo está localizado.

    Returns:
        DataFrame: Um DataFrame contendo os dados do arquivo CSV, ou None em caso de erro.
    """

    try:
        df_cars = pd.read_csv(diretorio_destino / 'cars.csv', sep=';')
        return df_cars
    except Exception as e:
        logging.error(f'Erro ao ler o arquivo CSV: {e}')
        return None


# ---------------------------------------------------------------------------------------
def limpar_e_tratar_dados(df_cars):

    """
    Realiza a limpeza e o tratamento dos dados em um DataFrame.

    Args:
        df_cars (DataFrame): O DataFrame contendo os dados a serem limpos e tratados.

    Returns:
        DataFrame: O DataFrame com os dados limpos e tratados.
    """

    try:
        df_cars = df_cars.drop(0)
        mapeamento_colunas = {
            "Car": "carro",
            "MPG": "milhas_por_galao",
            "Cylinders": "cilindros",
            "Displacement": "deslocamento",
            "Horsepower": "potencia",
            "Weight": "peso",
            "Acceleration": "aceleracao",
            "Model": "modelo",
            "Origin": "origem"
        }
        df_cars.rename(columns=mapeamento_colunas, inplace=True)
        return df_cars
    except Exception as e:
        logging.error(f'Erro ao dropar a linha: {e}')

# ---------------------------------------------------------------------------------------
def criar_diretorio_banco_de_dados(database):

    """
    Cria um diretório para armazenar o banco de dados SQLite.

    Args:
        database (str): O nome do banco de dados.

    Returns:
        str: O caminho para o diretório do banco de dados.
    """

    try:
        diretorio = os.path.dirname(__file__)
        diretorio_pasta = os.path.join(diretorio + f'/cadastro/{database}.db').replace('\\', '/')
        os.makedirs(diretorio_pasta, exist_ok=True)
        logging.info('Diretório database criado com sucesso.')
    except FileExistsError:
        print(f'{diretorio_pasta} database já existe.')
    
    return diretorio_pasta

# ---------------------------------------------------------------------------------------
def criar_tabela_de_carros(cursor):

    """
    Cria uma tabela no banco de dados SQLite para armazenar os dados.

    Args:
        cursor: O cursor utilizado para executar comandos SQL.
    """

    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_cars(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       carro TEXT,
                       milhas_por_galao FLOAT,
                       cilindros FLOAT,
                       deslocamento FLOAT,
                       potencia FLOAT,
                       peso FLOAT,
                       aceleracao FLOAT,
                       modelo TEXT,
                       origem TEXT
                    )""")
        print('Tabela criada com sucesso.')
    except sqlite3.Error as e:
        logging.error(f'Erro ao criar a tabela: {e}')


# ---------------------------------------------------------------------------------------
def inserir_registros_na_tabela(cursor, conn, df_cars_tranformado):

    """
    Insere registros na tabela do banco de dados.

    Args:
        cursor: O cursor utilizado para executar comandos SQL.
        conn: A conexão com o banco de dados.
        df_cars_tranformado: O DataFrame contendo os dados a serem inseridos na tabela.
    """

    try:
        for index, row in df_cars_tranformado.iterrows():
            cursor.execute(""" INSERT INTO tb_cars(
                           carro, milhas_por_galao, cilindros, deslocamento, potencia,
                           peso, aceleracao, modelo, origem)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           (row['carro'], row['milhas_por_galao'], row['cilindros'], row['deslocamento'], row['potencia'],
                            row['peso'], row['aceleracao'], row['modelo'], row['origem']))

        conn.commit()
        print('Dados inseridos na tabela com sucesso.')
    
    except sqlite3.Error as e:
        logging.error(f'Erro ao inserir dados na tabela: {e}')

# ---------------------------------------------------------------------------------------
def main():

    """
    Função principal que coordena o processo de download, leitura e manipulação de dados.
    """

    pasta = 'veiculos'
    diretorio_destino = criar_diretorio_de_destino(pasta)
    logging.info(f'Diretório Destino: {diretorio_destino}')

    base_url_cars = 'https://perso.telecom-paristech.fr/eagan/class/as2013/inf229/data/cars.csv'
    database = 'cadastro'
    
    if diretorio_destino:
        if baixar_arquivo_csv(base_url_cars, diretorio_destino):
            logging.info('Arquivo baixado com sucesso!')
            df_cars = ler_arquivo_csv(diretorio_destino)
            if df_cars is not None:
                logging.info('Arquivo lido com sucesso!')
                df_cars_tranformado = limpar_e_tratar_dados(df_cars)
                if len(df_cars_tranformado) > 0:
                    print(df_cars_tranformado)
                    path_db = criar_diretorio_banco_de_dados(database)
                    print(f'Diretório Database: {path_db}')
                    if path_db:
                        conn = sqlite3.connect(path_db)
                        cursor = conn.cursor()
                        criar_tabela_de_carros(cursor)
                        if criar_tabela_de_carros:
                            inserir_registros_na_tabela(cursor, conn, df_cars_tranformado)
                    else:
                        logging.error('Não foi possível criar o diretório do banco de dados.')
                else:
                    logging.error('DataFrame vazio após a limpeza.')
            else:
                logging.error('Falha ao ler o arquivo.')
        else:
            logging.error('Falha ao baixar o arquivo.')
    else:
        logging.error('Falha ao criar o diretório de destino.')

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()