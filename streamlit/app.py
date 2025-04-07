# Importar as bibliotecas
import logging
import requests
import pandas as pd
import streamlit as st
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuração do logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level="INFO")

# ---------------------------------------------------------------------------
def criar_diretorio_destino(pasta):

    try:
        diretorio = Path(__file__).resolve().parent / f"datalake/bronze/{pasta}"
        diretorio.mkdir(parents=True, exist_ok=True)
        logging.info("Diretorio criado com sucesso.")
        return diretorio
    except Exception as e:
        logging.error(f'Falha ao criar diretório: {e}')

# ---------------------------------------------------------------------------
def baixar_arquivo_csv(base_url_csv, diretorio_destino):

    try:
        resposta = requests.get(base_url_csv)
        if resposta.status_code == 200:
            with open(diretorio_destino / "customers.csv", "wb") as arquivo:
                arquivo.write(resposta.content)
                logging.info('Arquivo baixado e salvo com sucesso.')
                return True
        else:
            logging.info(f"Falha ao baixar o arquivo. Status code: {resposta.status_code}")
            return False
    except Exception as e:
        logging.error(f'Erro ao baixar o arquivo: {e}')
        return False

# ---------------------------------------------------------------------------
def ler_arquivo_csv(diretorio_destino):

    try:
        df_customers = pd.read_csv(diretorio_destino / "customers.csv")
        return df_customers
    except Exception as e:
        logging.error(f'Erro ao ler o arquivo CSV: {e}')
        return None

# ---------------------------------------------------------------------------
def limpar_e_tratar_dados(df_customers):

    try:
        mapeamento_colunas = {
            "Index": "index",
            "Customer Id": "customer_id",
            "First Name": "first_name",
            "Last Name": "last_name",
            "Company": "company",
            "City": "city",
            "Country": "country",
            "Phone 1": "phone_1",
            "Phone 2": "phone_2",
            "Email": "email",
            "Subscription Date": "subscription_date",
            "Website": "website"
        }
        df_customers["data_ingestion"] = pd.to_datetime(datetime.now())
        df_customers.rename(columns=mapeamento_colunas, inplace=True)
        return df_customers
    except Exception as e:
        logging.error(f'Erro ao dropar a linha: {e}')

# ---------------------------------------------------------------------------
def salvar_dados(df_customers, diretorio_destino, nome_arquivo="customers_processed.csv"):

    try:
        df_customers.to_csv(diretorio_destino / nome_arquivo, index=False)
        logging.info(f'Dados salvos com sucesso em {nome_arquivo}.')
    except Exception as e:
        logging.error(f'Erro ao salvar o arquivo: {e}')

# ---------------------------------------------------------------------------
def carregar_dados(diretorio_destino):

    try:
        caminho_arquivo = diretorio_destino / "customers_processed.csv"
        logging.info(f"Caminho do arquivo transformado: {caminho_arquivo}")
        if caminho_arquivo.exists():
            df_customers_processed = pd.read_csv(caminho_arquivo)
            return df_customers_processed
        else:
            st.error("Arquivo não encontrado!")
            return None
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

# ---------------------------------------------------------------------------
def main():

    # Passo 1: Criar diretório de destino
    pasta = "customers"
    diretorio_destino = criar_diretorio_destino(pasta)
    logging.info(f"Diretorio destino: {diretorio_destino}")
    
    # Passo 2: Baixar arquivo CSV
    if diretorio_destino:
        base_url_csv = "https://drive.google.com/uc?id=1x2IdSNcHGLmot9i1h90gwMJr5lULC2QV&export=download"
        if baixar_arquivo_csv(base_url_csv, diretorio_destino):
            logging.info('Arquivo baixado com sucesso!')
            # Passo 3: Ler o arquivo CSV
            df_customers = ler_arquivo_csv(diretorio_destino)
            if df_customers is not None:
                # Passo 4: Limpar e transformar os dados
                df_customers_transf = limpar_e_tratar_dados(df_customers)
                if df_customers_transf is not None and len(df_customers_transf) > 0:
                    salvar_dados(df_customers, diretorio_destino, nome_arquivo="customers_processed.csv")

                    st.write("DADOS TRANSFORMADOS")
                    st.dataframe(df_customers_transf)
                else:
                    logging.error('DataFrame vazio após a limpeza.')
            else:
                logging.error('Falha ao ler o arquivo.')
        else:
            logging.error('Falha ao baixar o arquivo.')
    else:
        logging.error('Falha ao criar o diretório de destino.')

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()