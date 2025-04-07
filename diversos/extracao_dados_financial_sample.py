import os # Manipulação de caminhos de diretórios.
import sqlite3 # Conexão com o banco de dados SQLite
import logging # Criação de registros de eventos para o seu programa.
import requests # Permite fazer solicitações HTTP para baixar arquivos da internet
import pandas as pd
from pathlib import Path # Path de pathlib: É uma maneira mais moderna de manipular caminhos de arquivos e diretórios.

# -----------------------------------------------------------------------------------------------------------
# 1. Criar diretório de destino - OK
# 2. Download do arquivo TXT
# 3. Diretório do banco de dados
# 4. Leitura do arquivo
# 5. Criar a tabela
# 6. Inserir registros na tabela
# 7. Popular os dados no banco de dados SQLite

# -----------------------------------------------------------------------------------------------------------
def criar_diretorio(folder):

    """
    Cria um diretório de destino para salvar o arquivo baixado.

    Args:
        folder (str): O nome do diretório a ser criado.

    Returns:
        Path: O caminho completo para o diretório criado.
    """

    try:
        diretorio = Path(__file__).resolve().parent / f'datalake/bronze/{folder}'
        diretorio.mkdir(parents=True, exist_ok=True)
        logging.info(f'Diretório {diretorio} criado com sucesso.')
        return diretorio
    except Exception as e:
        logging.error(f'Erro ao criar o diretório: {e}')
        return None

# -----------------------------------------------------------------------------------------------------------
def download_arquivo(BASE_URL, diretorio_destino):

    """
    Baixa um arquivo da internet e salva-o no diretório especificado.
    
    Args:
        url (str): O URL do arquivo a ser baixado.
        destino (Path): O caminho completo para o diretório onde o arquivo será salvo.
    
    Returns:
        bool: True se o arquivo foi baixado com sucesso, False caso contrário.
    """

    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            with open(diretorio_destino / 'financial_sample.xlsx', 'wb') as arquivo:
                arquivo.write(response.content)
                logging.info('Arquivo baixado e salvo com sucesso.')
                return True
        else:
            print(f'Falha ao baixar o arquivo. Status code: {response.status_code}')
            return False
    except Exception as e:
        logging.error(f'Erro ao baixar o arquivo: {e}')
        return False

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
        BASE_PATH = os.path.dirname(__file__)
        BASE_FOLDER = os.path.join(BASE_PATH + f'/cadastro/{database}.db').replace('\\', '/')
        os.makedirs(BASE_FOLDER, exist_ok=True)
        print(f'{BASE_FOLDER} database criado com sucesso.')
    except FileExistsError:
        print(f'{BASE_FOLDER} database já existe.')

    return BASE_FOLDER

# -----------------------------------------------------------------------------------------------------------
def leitura_arquivo(diretorio_destino):

    try:
        # Lê a planilha Excel em um DataFrame
        df_arquivo = pd.read_excel(diretorio_destino / 'financial_sample.xlsx')
        return df_arquivo
    except Exception as e:
        logging.error(f'Erro ao ler o arquivo Excel: {e}')
        return None

# -----------------------------------------------------------------------------------------------------------
def criar_tabela(cursor):

    try:
        # Criar a tabela, se caso não existir
        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_financial_sample (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        segment TEXT,
                        country TEXT,
                        product TEXT,
                        discount_band TEXT,
                        units_sold FLOAT,
                        manufacturing_price FLOAT,
                        sale_price FLOAT,
                        gross_sales FLOAT,
                        discounts FLOAT,
                        sales FLOAT,
                        cogs TEXT,
                        profit FLOAT,
                        date DATE,
                        month_number INTEGER,
                        month_name TEXT,
                        year INTEGER
                        )""")
        
        print('Tabela criada com sucesso.')
        
    except sqlite3.Error as e:
        logging.error(f'Erro ao criar a tabela: {e}')

# -----------------------------------------------------------------------------------------------------------
def inserir_dados(cursor, conn, df_tabela):

    try:
        df_tabela['Manufacturing Price'] = df_tabela['Manufacturing Price'].str.replace('R\$', '').str.replace(',', '')
        df_tabela['Sale Price'] = df_tabela['Sale Price'].str.replace('R\$', '').str.replace(',', '')
        df_tabela['Gross Sales'] = df_tabela['Gross Sales'].str.replace('R\$', '').str.replace(',', '')
        df_tabela['Discounts'] = df_tabela['Discounts'].str.replace('R\$', '').str.replace(',', '')
        df_tabela[' Sales'] = df_tabela[' Sales'].str.replace('R\$', '').str.replace(',', '')
        df_tabela['COGS'] = df_tabela['COGS'].str.replace('R\$', '').str.replace(',', '')
        df_tabela['Profit'] = df_tabela['Profit'].str.replace('R\$', '').str.replace(',', '')
        df_tabela = df_tabela.rename(columns=lambda x: x.strip())
        for index, row in df_tabela.iterrows():
            cursor.execute("""INSERT INTO tb_financial_sample(
                               segment, country, product, discount_band,
                               units_sold, manufacturing_price, sale_price, gross_sales,
                               discounts, sales, cogs, profit,
                               date, month_number, month_name, year)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           (row['Segment'], row['Country'], row['Product'], row['Discount Band'],
                            row['Units Sold'], row['Manufacturing Price'], row['Sale Price'], row['Gross Sales'],
                            row['Discounts'], row['Sales'], row['COGS'], row['Profit'],
                            row['Date'], row['Month Number'], row['Month Name'], row['Year']))
        conn.commit()
        print('Dados inseridos na tabela com sucesso.')

    except sqlite3.Error as e:
        logging.error(f'Erro ao inserir dados na tabela: {e}')

# -----------------------------------------------------------------------------------------------------------
def main():

    folder = 'financial_sample'
    BASE_URL = 'https://go.microsoft.com/fwlink/?LinkID=521962'
    
    diretorio_destino = criar_diretorio(folder) # Chamada da função
    print(f'Diretório do Arquivo: {diretorio_destino}')
    if diretorio_destino:
        if download_arquivo(BASE_URL, diretorio_destino): # Chamada da função
            print('Arquivo baixado com sucesso!')
        else:
            print('Falha ao baixar o arquivo.')

    # Conectar ao banco de dados SQLite
    database = 'cadastro'
    PATH_DB = diretorio_db(database) # Chamada da função
    if PATH_DB:
        conn = sqlite3.connect(PATH_DB)
        # Criar cursor
        cursor = conn.cursor()

        criar_tabela(cursor) # Chamada da função
        
        df_tabela = leitura_arquivo(diretorio_destino) # Chamada da função
        if df_tabela is not None:
            inserir_dados(cursor, conn, df_tabela) # Chamada da função
        else:
            logging.error('Não foi possível ler o arquivo Excel.')

    else:
        logging.error('Não foi possível criar o diretório do banco de dados.')

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()