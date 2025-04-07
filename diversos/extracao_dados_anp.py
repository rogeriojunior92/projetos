# Importações
import os
import sqlite3
import zipfile
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
"""
Passo a passo
1. Criar o diretório caso ele não exista.
2. Baixar o arquivo ZIP (compactado) para o local desejado.
3. Extrair o conteúdo do arquivo ZIP.
4. Efetuar a leitura do(s) arquivo(s) extraído(s).
5. Limpar e tratar os dados:
    1. Concatenar os DataFrames.
    2. Renomear as colunas conforme necessário.
6. Criar tabela caso ele não exista.
7. Inserir registros na tabela.
"""

# ---------------------------------------------------------------------------
# Função para criar o diretório caso ele não exista.
def criar_diretorio(pasta):
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
        logging.info("Diretorio criado com sucesso.")
        return diretorio
    except Exception as e:
        logging.error(f"Falha ao criar diretorio: {e}")

# ---------------------------------------------------------------------------
# Função para baixar o arquivo ZIP (compactado) para o local desejado.
def baixar_arquivos(lista_urls, diretorio_destino):
    """
    Baixa um arquivo CSV comprimido (.gz) de uma URL e o salva no diretório de destino.
    
    Parâmetros:
    base_url (str): A URL do arquivo CSV comprimido.
    diretorio_destino (Path): O diretório onde o arquivo será salvo.
    
    Retorna:
    bool: Retorna True se o arquivo for baixado e salvo com sucesso, False em caso de erro.
    """
    try:
        for lista in lista_urls:
            nome_arquivo = lista.split("/")[-3]
            resposta = requests.get(lista)
            if resposta.status_code == 200:
                with open(diretorio_destino / nome_arquivo, "wb") as arquivo:
                    arquivo.write(resposta.content)
                    logging.info(f'Arquivo baixado e salvo com sucesso: {nome_arquivo}')
            else:
                logging.error(f'Falha ao baixar o arquivo. Status code: {resposta.status_code}')
                return False
        return True
    except Exception as e:
        logging.error(f'Erro ao baixar o arquivo: {e}')
        return False

# ---------------------------------------------------------------------------
# Função para extrair o conteúdo do arquivo ZIP.
def descompactar_arquivo(diretorio_destino, lista_urls):
    """
    Descompacta um arquivo CSV comprimido (.gz) no diretório de destino.
    
    Parâmetros:
    diretorio_destino (Path): O diretório onde o arquivo comprimido será descompactado.
    
    Retorna:
    bool: Retorna True se o arquivo for descompactado com sucesso, False em caso de erro.
    """
    try:
        for lista in lista_urls:
            nome_arquivo = lista.split("/")[-3]
            arquivo_zip = diretorio_destino / f"{nome_arquivo}"
            
            # Usando zipfile para extrair o conteúdo
            with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
                zip_ref.extractall(diretorio_destino)
                logging.info(f"Conteúdo do arquivo {nome_arquivo}.zip extraído com sucesso.")
        return True
    except Exception as e:
        logging.error(f"Falha ao descompactar arquivo ZIP: {e}")
        return False

# ---------------------------------------------------------------------------
# Função para efetuar a leitura do(s) arquivo(s) extraído(s).
def ler_arquivo(diretorio_destino):
    """
    Lê um arquivo CSV e retorna um DataFrame com os dados.
    
    Parâmetros:
    diretorio_destino (Path): O diretório onde o arquivo CSV descompactado está localizado.
    
    Retorna:
    pd.DataFrame: Um DataFrame contendo os dados do CSV, ou None em caso de erro.
    """
    try:
        arquivo_ca202401 = diretorio_destino / "Preços semestrais - AUTOMOTIVOS_2024.01.csv"
        arquivo_ca202402 = diretorio_destino / "Preços semestrais - AUTOMOTIVOS_2024.02.csv"

        if arquivo_ca202401.exists() and arquivo_ca202402.exists():
            df_ca202401 = pd.read_csv(arquivo_ca202401, delimiter=";", on_bad_lines="skip")
            df_ca202402 = pd.read_csv(arquivo_ca202402, delimiter=";", on_bad_lines="skip")

            logging.info("Arquivos lidos com sucesso.")
            return df_ca202401, df_ca202402
        else:
            logging.error("Um ou mais arquivos não encontrados.")
            return None, None
    except Exception as e:
        logging.error(f"Falha na leitura do arquivo: {e}")
        return None, None

# ---------------------------------------------------------------------------
# Função para limpar e tratar os dados
def limpar_e_tratar_dados(df_ca202401, df_ca202402):
    """
    Realiza a limpeza e transformação dos dados, como conversão de datas e cálculo de taxa de mortalidade.
    
    Parâmetros:
    df_casos (pd.DataFrame): O DataFrame contendo os dados brutos.
    
    Retorna:
    pd.DataFrame: O DataFrame transformado, com as colunas selecionadas e os dados processados.
    """
    try:
        df_transf = pd.concat([df_ca202401, df_ca202402])
        logging.info("Arquivos combinados com sucesso.")

        df_transf["data_ingestao"] = pd.to_datetime("now")
        colunas_rename = {
            "Regiao - Sigla": "regiao_sigla",
            "Estado - Sigla": "estado_sigla",
            "Municipio": "municipio",
            "Revenda": "revenda",
            "CNPJ da Revenda": "cnpj_revenda",
            "Nome da Rua": "nome_rua",
            "Numero Rua": "numero_rua",
            "Complemento": "complemento",
            "Bairro": "bairro",
            "Cep": "cep",
            "Produto": "produto",
            "Data da Coleta": "data_coleta",
            "Valor de Venda": "valor_venda",
            "Valor de Compra": "valor_compra",
            "Unidade de Medida": "unidade_medida",
            "Bandeira": "bandeira"
        }
        df_transf.rename(columns=colunas_rename, inplace=True)       
        return df_transf
    except Exception as e:
        logging.error(f"Falha durante a combinação de arquivos: {e}")

# ---------------------------------------------------------------------------
def salvar_dataframe(diretorio_destino, df_transf):
    """
    Salva o DataFrame em um arquivo CSV no diretório de destino.
    
    Parâmetros:
    diretorio_destino (Path): O diretório onde o arquivo CSV será salvo.
    df_transf (pd.DataFrame): O DataFrame que será salvo.
    """
    try:
        arquivo_saida = diretorio_destino / "anp_ca_transformado.csv"
        df_transf.to_csv(arquivo_saida, index=False)
        logging.info(f"DataFrame salvo com sucesso em: {arquivo_saida}")
    except Exception as e:
        logging.error(f"Erro ao salvar o DataFrame: {e}")

# ---------------------------------------------------------------------------
# Função para criar tabela caso ele não exista
def criar_tabela(cursor):
    """
    Cria a tabela no banco de dados se não existir, com a estrutura necessária para armazenar os dados.
    
    Parâmetros:
    cursor (sqlite3.Cursor): O cursor do banco de dados para executar o comando SQL.
    """
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS tbl_anp(
                       regiao_sigla TEXT,
                       estado_sigla TEXT,
                       municipio TEXT,
                       revenda TEXT,
                       cnpj_revenda TEXT,
                       nome_rua TEXT,
                       complemento TEXT,
                       bairro TEXT,
                       cep INTEGER,
                       produto TEXT,
                       data_coleta TEXT,
                       valor_venda FLOAT,
                       valor_compra FLOAT,
                       unidade_medida FLOAT,
                       bandeira TEXT,
                       data_ingestao TEXT
                       )""")
        logging.info("Tabela criado com sucesso.")
    except sqlite3.Error as e:
        logging.error(f'Erro ao criar a tabela: {e}')

# ---------------------------------------------------------------------------
# Função para inserir registros na tabela.
def inserir_registros():
    """
    Cria a tabela no banco de dados se não existir, com a estrutura necessária para armazenar os dados.
    
    Parâmetros:
    cursor (sqlite3.Cursor): O cursor do banco de dados para executar o comando SQL.
    """
    pass

# ---------------------------------------------------------------------------
def main():
    """
    Função principal que executa todo o processo.
    """
    pasta = "dados_abertos"
    diretorio_destino = criar_diretorio(pasta)
    logging.info(f"Diretorio destino: {diretorio_destino}")
    
    if diretorio_destino:
        lista_urls = ["https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-2024-01.zip/@@download/file",
                      "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-2024-02.zip/@@download/file"]
        if baixar_arquivos(lista_urls, diretorio_destino):
            if descompactar_arquivo(diretorio_destino, lista_urls):
                df_ca202401, df_ca202402 = ler_arquivo(diretorio_destino)
                if df_ca202401 is not None and df_ca202402 is not None:
                    df_transf = limpar_e_tratar_dados(df_ca202401, df_ca202402)
                    if df_transf is not None:
                        salvar_dataframe(diretorio_destino, df_transf)
                        path_db = os.getenv("PATH_DB")
                        if path_db:
                            conn = sqlite3.connect(path_db)
                            cursor = conn.cursor()
                            criar_tabela(cursor)
                        else:
                            logging.error('Caminho do banco de dados não encontrado.')
                    else:
                        logging.error("Falha ao tratar e limpar os dados.")
                else:
                    logging.error("Falha ao ler os arquivos após a descompactação.")
            else:
                logging.error("Falha ao descompactar o arquivo.")
        else:
            logging.error("Falha ao baixar arquivo.")
    else:
        logging.error('Falha ao criar diretório.')

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()