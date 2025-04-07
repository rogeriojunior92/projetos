# Importar as bibliotecas
import sqlite3
import logging
import pandas as pd
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuração do logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level="INFO")

# ---------------------------------------------------------------------------
"""
1. Conectar no banco de dados SQLite
2. Extrair dados da tabela
3. Salvar no Dataframe
"""

# ---------------------------------------------------------------------------
def diretorio_banco_de_dados(database):
    """
    Função para garantir que o diretório do banco de dados exista.
    :param database: Nome do banco de dados (sem a extensão .db).
    :return: Caminho completo do banco de dados.
    """
    try:
        diretorio = Path(__file__).resolve().parent / "datalake" / "database"
        diretorio.mkdir(parents=True, exist_ok=True) # Criando o diretório, se não existir
        logging.info(f'Diretório para o banco de dados criado em: {diretorio}')

        # Caminho completo para o banco de dados
        caminho_banco = diretorio / f"{database}.db"
        return caminho_banco
    except FileExistsError as e:
        logging.error(f'{diretorio} database já existe: {e}')

# ---------------------------------------------------------------------------
def conexao_sqlite(caminho_banco):
    """
    Função para estabelecer a conexão com o banco de dados SQLite.
    :param caminho_db: Caminho completo do banco de dados.
    :return: Conexão com o banco de dados SQLite.
    """
    try:
        conn = sqlite3.connect(caminho_banco)
        logging.info(f"Conexão estabelecida com o banco de dados: {caminho_banco}")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# ---------------------------------------------------------------------------
def extrair_dados_tabela(conn, tabela):
    """
    Função para extrair dados de uma tabela específica no banco de dados.
    :param conn: Conexão com o banco de dados SQLite.
    :param tabela: Nome da tabela a ser consultada.
    :return: Lista de tuplas com os dados extraídos da tabela.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela}")
        dados = cursor.fetchall()
        logging.info(f"Dados extraídos com sucesso da tabela '{tabela}'.")
        return dados
    except sqlite3.Error as e:
        logging.error(f"Erro ao extrair dados da tabela '{tabela}': {e}")
        return []

# ---------------------------------------------------------------------------
def salvar_df(dados, colunas):
    """
    Função para salvar os dados extraídos em um DataFrame do pandas.
    :param dados: Dados extraídos, em formato de lista de tuplas.
    :param colunas: Lista de colunas para nomear as colunas no DataFrame.
    :return: DataFrame com os dados extraídos.
    """
    try:
        df_cars = pd.DataFrame(dados, columns=colunas)
        logging.info(f"DataFrame criado com {len(df_cars)} registros.")
        return df_cars
    except Exception as e:
        logging.error(f"Nenhum dado para salvar no DataFrame: {e}")
        return None

# ---------------------------------------------------------------------------
def main():
    """
    Função principal para controlar o fluxo de execução.
    """
    database = "cadastro"
    caminho_db = diretorio_banco_de_dados(database)

    if caminho_db:
        logging.info(f"Caminho do banco de dados: {caminho_db}")
        conn = conexao_sqlite(caminho_db)
        if conn:
            tabela = "tb_cars"
            dados = extrair_dados_tabela(conn, tabela)
            if dados:
                colunas = ["id", "carro", "milhas_por_galao", "cilindros", "deslocamento", "potencia", "peso", "aceleracao", "modelo", "origem"]
                df_cars = salvar_df(dados, colunas)
                if df_cars is not None:
                    print(df_cars)
            else:
                logging.error(f"Não há dados para a tabela '{tabela}'.")
        else:
            logging.error("Falha ao estabelecer a conexão com o banco de dados.")
    else:
        logging.error("Não foi possível obter o diretório do banco de dados.")
    
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
