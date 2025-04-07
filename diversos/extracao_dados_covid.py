import os
import sqlite3
import logging
import requests
import pandas as pd
from pathlib import Path # Manipular caminhos de arquivos e diretórios.

# -----------------------------------------------------------------------------------------------------------
# 1. Criar diretório
# 2. Download do arquivo
# 3. Limpeza / Tratamento dos dados
# 4. Criar diretório do banco de dados
# 5. Criar a tabela
# 6. Inserir registros no banco de dados

# -----------------------------------------------------------------------------------------------------------
def criar_diretorio(folder):
    
    try:
        diretorio = Path(__file__).resolve().parent / f'datalake/bronze/{folder}'.replace('\\', '/')
        diretorio.mkdir(parents=True, exist_ok=True)
        logging.info('Diretório criado com sucesso.')
        return diretorio
    except Exception as e:
        logging.error(f'Falha ao criar diretorio: {e}')
        return None

# -----------------------------------------------------------------------------------------------------------
def download_arquivo(diretorio_destino, base_url):

    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            with open(diretorio_destino / 'enterprise_survey_2021.csv', 'wb') as arquivo:
                arquivo.write(response.content)
                logging.info('Arquivo baixado e salvo com sucesso.')
                return True
        else:
            logging.error(f'Erro ao baixar o arquivo: {e}')
            return False
    except Exception as e:
        logging.error(f'Falha ao baixar o arquivo. Status code: {response.status_code}')
        return False

# -----------------------------------------------------------------------------------------------------------
def leitura_arquivo(diretorio_destino):
    
    try:
        df_covid = pd.read_csv(diretorio_destino / 'enterprise_survey_2021.csv')
        logging.info('Leitura do arquivo com sucesso.')
        return df_covid
    except Exception as e:
        logging.error(f'Erro ao ler o arquivo CSV: {e}')
        return None

# -----------------------------------------------------------------------------------------------------------
def limpeza_dados(df_covid):

    # Dicionário com os mapeamentos de nome atual para novo nome
    mapeamento_colunas = {
        'Year': 'ano',
        'Industry_aggregation_NZSIOC': 'agregacao_industria_nzsioc',
        'Industry_code_NZSIOC': 'codigo_industria_nzsioc',
        'Industry_name_NZSIOC': 'nome_industria_nzsioc',
        'Units': 'unidades',
        'Variable_code': 'codigo_variavel',
        'Variable_name': 'nome_variavel',
        'Variable_category': 'categoria_variavel',
        'Value': 'valor',
        'Industry_code_ANZSIC06': 'codigo_industria_nzsioc06'
    }

    # O método rename para renomear as colunas
    df_covid.rename(columns=mapeamento_colunas, inplace=True)
    return df_covid

# -----------------------------------------------------------------------------------------------------------
def diretorio_db(database):
    
    try:
        diretorio = os.path.dirname(__file__)
        diretorio_folder = os.path.join(diretorio + f'/cadastro/{database}.db').replace('\\', '/')
        os.makedirs(diretorio_folder, exist_ok=True)
        logging.info(f'Diretório criado com sucesso: {diretorio_folder}')
    except FileExistsError:
        print(f'{diretorio_folder} database já existe.')
    
    return diretorio_folder
    
# -----------------------------------------------------------------------------------------------------------
def criar_tabela(cursor):
    
    try:
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tb_enterprise_survey(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ano INTEGER,
                    agregacao_industria_nzsioc TEXT,
                    codigo_industria_nzsioc INTEGER
                    nome_industria_nzsioc TEXT
                    unidades TEXT
                    codigo_variavel TEXT
                    nome_variavel TEXT
                    categoria_variavel TEXT
                    valor FLOAT
                    codigo_industria_nzsioc06 TEXT
                        )""")
        
        print('Tabela criada com sucesso.')

    except sqlite3.Error as e:
        logging.error(f'Erro ao criar a tabela: {e}')

# -----------------------------------------------------------------------------------------------------------
def inserir_dados_db(conn, cursor, df_covid):
    
    try:
        for index, row in df_covid.iterrows():
            cursor.execute("""
                        INSERT INTO tb_enterprise_survey(
                            ano, agregacao_industria_nzsioc, codigo_industria_nzsioc, nome_industria_nzsioc, unidades,
                            codigo_variavel, categoria_variavel, valor, codigo_industria_nzsioc06)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (row['ano'], row['agregacao_industria_nzsioc'], row['codigo_industria_nzsioc'], row['nome_industria_nzsioc'], row['unidades'],
                         row['codigo_variavel'], row['categoria_variavel'], row['valor'], row['codigo_industria_nzsioc06']))
            
        conn.commit()
        print('Dados inseridos na tabela com sucesso.')

    except sqlite3.Error as e:
        logging.error(f'Erro ao inserir dados na tabela: {e}')

# -----------------------------------------------------------------------------------------------------------
def main():
    
    folder = 'enterprise_survey_2021'
    base_url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
    
    diretorio_destino = criar_diretorio(folder) # Chamada da função
    print(f'Diretório Destino: {diretorio_destino}')
    
    if diretorio_destino:  
        download_arquivo(diretorio_destino, base_url) # Chamada da função
        print(f'Diretório Destino: {diretorio_destino}')
    else:
        print('Falha ao baixar o arquivo.')
    
    df_covid = leitura_arquivo(diretorio_destino) # Chamada da função
    
    database = 'cadastro'
    diretorio_database = diretorio_db(database) # Chamada da função
    if diretorio_database:
        conn = sqlite3.connect(diretorio_database)
        cursor = conn.cursor()
        criar_tabela(cursor) # Chamada da função

        df_covid_transformado = limpeza_dados(df_covid) # Chamada da função
        if df_covid_transformado:
            inserir_dados_db(conn, cursor, df_covid)
        else:
            logging.error('Não foi possível ler o arquivo Excel.') # Chamada da função
    else:
        logging.error('Não foi possível criar o diretório do banco de dados.')

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()