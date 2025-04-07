# Importações
import os
import gzip
import shutil
import logging
import sqlite3
import requests
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Carrega as variáveis do arquivo .env
load_dotenv()

# ---------------------------------------------------------------------------
# Configuração do logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level="INFO")

# ---------------------------------------------------------------------------
def criar_diretorio(pasta: str) -> Path:
    """
    Cria um diretório dentro de 'datalake/bronze' com o nome fornecido, se não existir.
    
    Parâmetros:
    pasta (str): O nome da pasta a ser criada.
    
    Retorna:
    Path: O caminho do diretório criado ou None se ocorrer erro.
    """
    try:
        diretorio = Path(__file__).resolve().parent / f"datalake/bronze/{pasta}"
        diretorio.mkdir(parents=True, exist_ok=True)
        logging.info(f"Diretorio criado com sucesso: {diretorio}")
        return diretorio
    except Exception as e:
        logging.error(f"Falha ao criar diretorio: {e}")
        return None

# ---------------------------------------------------------------------------
def baixar_arquivo_csv(base_url: str, diretorio_destino: Path) -> bool:
    """
    Baixa um arquivo CSV comprimido (.gz) de uma URL e o salva no diretório de destino.
    
    Parâmetros:
    base_url (str): A URL do arquivo CSV comprimido.
    diretorio_destino (Path): O diretório onde o arquivo será salvo.
    
    Retorna:
    bool: Retorna True se o arquivo for baixado e salvo com sucesso, False em caso de erro.
    """
    try:
        resposta = requests.get(base_url)
        if resposta.status_code == 200:
            with open(diretorio_destino / "caso.csv.gz", "wb") as arquivo:
                arquivo.write(resposta.content)
            logging.info('Arquivo baixado e salvo com sucesso.')
            return True
        else:
            logging.error(f'Falha ao baixar o arquivo. Status code: {resposta.status_code}')
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f'Erro ao baixar o arquivo: {e}')
        return False

# ---------------------------------------------------------------------------
def descompactar_arquivo(diretorio_destino: Path) -> bool:
    """
    Descompacta um arquivo CSV comprimido (.gz) no diretório de destino.
    
    Parâmetros:
    diretorio_destino (Path): O diretório onde o arquivo comprimido será descompactado.
    
    Retorna:
    bool: Retorna True se o arquivo for descompactado com sucesso, False em caso de erro.
    """
    try:
        with gzip.open(diretorio_destino / "caso.csv.gz", "rb") as entrada:
            with open(diretorio_destino / "caso.csv", "wb") as saida:
                shutil.copyfileobj(entrada, saida)
        logging.info("Arquivo descompactado com sucesso.")
        return True
    except Exception as e:
        logging.error(f"Falha ao descompactar arquivo: {e}")
        return False

# ---------------------------------------------------------------------------
def leitura_arquivo_csv(diretorio_destino: Path) -> pd.DataFrame:
    """
    Lê um arquivo CSV e retorna um DataFrame com os dados.
    
    Parâmetros:
    diretorio_destino (Path): O diretório onde o arquivo CSV descompactado está localizado.
    
    Retorna:
    pd.DataFrame: Um DataFrame contendo os dados do CSV, ou None em caso de erro.
    """
    try:
        df_casos = pd.read_csv(diretorio_destino / "caso.csv")
        logging.info("Arquivo lido com sucesso.")
        return df_casos
    except Exception as e:
        logging.error(f"Falha na leitura do arquivo: {e}")
        return None

# ---------------------------------------------------------------------------
def tratar_e_limpar_dados(df_casos: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza a limpeza e transformação dos dados, como conversão de datas e cálculo de taxa de mortalidade.
    
    Parâmetros:
    df_casos (pd.DataFrame): O DataFrame contendo os dados brutos.
    
    Retorna:
    pd.DataFrame: O DataFrame transformado, com as colunas selecionadas e os dados processados.
    """
    try:
        df_casos["date"] = pd.to_datetime(df_casos["date"], errors="coerce")
        df_casos["year"] = df_casos["date"].dt.year
        df_casos["death_rate"] = df_casos["deaths"] / df_casos["confirmed"]
        df_casos["is_last"] = df_casos["is_last"].map({True: 1, False: 0})
        colunas_selecionadas = ['date', 'year', 'state', 'city', 'city_ibge_code', 'place_type', 'order_for_place', 
                                'confirmed', 'deaths', 'confirmed_per_100k_inhabitants', 'death_rate', 
                                'estimated_population_2019', 'estimated_population', 'is_last']
        return df_casos[colunas_selecionadas]
    except Exception as e:
        logging.error(f"Falha na transformação dos dados: {e}")
        return df_casos

# ---------------------------------------------------------------------------
def salvar_dataframe(diretorio_destino: Path, df_selecionado: pd.DataFrame):
    """
    Salva o DataFrame em um arquivo CSV no diretório de destino.
    
    Parâmetros:
    diretorio_destino (Path): O diretório onde o arquivo CSV será salvo.
    df_selecionado (pd.DataFrame): O DataFrame que será salvo.
    """
    try:
        arquivo_saida = diretorio_destino / "covid_transformado.csv"
        df_selecionado.to_csv(arquivo_saida, index=False)
        logging.info(f"DataFrame salvo com sucesso em: {arquivo_saida}")
    except Exception as e:
        logging.error(f"Erro ao salvar o DataFrame: {e}")

# ---------------------------------------------------------------------------
def criar_tabela(cursor: sqlite3.Cursor):
    """
    Cria a tabela no banco de dados se não existir, com a estrutura necessária para armazenar os dados.
    
    Parâmetros:
    cursor (sqlite3.Cursor): O cursor do banco de dados para executar o comando SQL.
    """
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS tbl_covid(
                        date TEXT,
                        year INTEGER,
                        state TEXT,
                        city TEXT,
                        city_ibge_code INTEGER,
                        place_type TEXT,
                        order_for_place INTEGER,
                        confirmed FLOAT,
                        deaths FLOAT,
                        confirmed_per_100k_inhabitants FLOAT,
                        death_rate FLOAT,
                        estimated_population_2019 FLOAT,
                        estimated_population FLOAT,
                        is_last INTEGER                 
                      )""")
        logging.info('Tabela criada com sucesso.')
    except sqlite3.Error as e:
        logging.error(f'Erro ao criar a tabela: {e}')

# ---------------------------------------------------------------------------
def inserir_registros_tabela(df_transf: pd.DataFrame, cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    """
    Insere os dados do DataFrame transformado na tabela do banco de dados.
    
    Parâmetros:
    df_transf (pd.DataFrame): O DataFrame contendo os dados transformados.
    cursor (sqlite3.Cursor): O cursor do banco de dados para executar os comandos SQL.
    conn (sqlite3.Connection): A conexão com o banco de dados.
    """
    try:
        cursor.execute("DELETE FROM tbl_covid")
        for _, row in df_transf.iterrows():
            cursor.execute(""" INSERT INTO tbl_covid(
                               date, year, state, city, city_ibge_code, place_type, order_for_place, confirmed, 
                               deaths, confirmed_per_100k_inhabitants, death_rate, estimated_population_2019,
                               estimated_population, is_last)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                               (row['date'], row['year'], row['state'], row['city'], row['city_ibge_code'], 
                                row['place_type'], row['order_for_place'], row['confirmed'], 
                                row['deaths'], row['confirmed_per_100k_inhabitants'], row['death_rate'], 
                                row['estimated_population_2019'], row['estimated_population'], row['is_last']))
        conn.commit()
        logging.info(f'Dados inseridos na tabela com sucesso. Total de registros: {len(df_transf)}')
    except sqlite3.Error as e:
        logging.error(f'Erro ao inserir dados na tabela: {e}')

# ---------------------------------------------------------------------------
def main():
    """
    Função principal que executa todo o processo.
    """
    pasta = "covid19"
    diretorio_destino = criar_diretorio(pasta)
    if diretorio_destino:
        base_url = "https://data.brasil.io/dataset/covid19/caso.csv.gz"
        if baixar_arquivo_csv(base_url, diretorio_destino):
            if descompactar_arquivo(diretorio_destino):
                df_casos = leitura_arquivo_csv(diretorio_destino)
                if df_casos is not None and not df_casos.empty:
                    df_casos_transf = tratar_e_limpar_dados(df_casos)
                    if df_casos_transf is not None:
                        salvar_dataframe(diretorio_destino, df_casos_transf)
                        path_db = os.getenv("PATH_DB")
                        if path_db:
                            conn = sqlite3.connect(path_db)
                            cursor = conn.cursor()
                            criar_tabela(cursor)
                            inserir_registros_tabela(df_casos_transf, cursor, conn)
                        else:
                            logging.error('Caminho do banco de dados não encontrado.')
                    else:
                        logging.error("Falha ao tratar e limpar os dados.")
                else:
                    logging.error("Erro ao carregar dados do arquivo CSV.")
            else:
                logging.error("Falha ao descompactar o arquivo.")
        else:
            logging.error("Falha ao baixar arquivo.")
    else:
        logging.error('Falha ao criar diretório.')

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
