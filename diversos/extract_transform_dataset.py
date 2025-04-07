# Importar as bibliotecas
import logging
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuração do logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level="INFO")

# ---------------------------------------------------------------------------
"""
O fluxo geral do script é:
1. Criar um diretório de destino se não existir.
2. Baixar um arquivo C  SV de uma URL fornecida.
3. Ler o arquivo CSV e tratar os dados:
   - Adicionar um novo campo "idade" calculado com base no ano de nascimento.
   - Adicionar um campo "geração" baseado na idade (Geração X, Y ou Z).
   - Renomear as colunas para um formato mais amigável.
4. Salvar os dados transformados em um arquivo CSV.
5. Logs são gerados para cada etapa importante do processo.
"""

# ---------------------------------------------------------------------------
def criar_diretorio_destino(pasta):
    """
    Cria um diretório no caminho especificado. Caso o diretório já exista, nada é feito.

    Parâmetros:
    pasta (str): Nome da pasta que será criada dentro do caminho especificado.

    Retorna:
    Path: Objeto Path do diretório criado ou existente.
    """
    try:
        diretorio = Path(__file__).resolve().parent / f"datalake/bronze/{pasta}"
        diretorio.mkdir(parents=True, exist_ok=True)
        logging.info("Diretorio criado com sucesso.")
        return diretorio
    except Exception as e:
        logging.error(f"Diretório já existe: {e}")

# ---------------------------------------------------------------------------
def baixar_csv(base_url, diretorio_destino):
    """
    Baixa um arquivo CSV a partir de uma URL e o salva no diretório de destino.

    Parâmetros:
    base_url (str): URL de onde o arquivo CSV será baixado.
    diretorio_destino (Path): Caminho onde o arquivo CSV será salvo.

    Retorna:
    bool: True se o arquivo foi baixado e salvo com sucesso, False caso contrário.
    """
    try:
        resposta = requests.get(base_url)
        if resposta.status_code == 200:
            with open(diretorio_destino / "people.csv", "wb") as arquivo:
                arquivo.write(resposta.content)
                logging.info("Arquivo baixado e salvo com sucesso.")
                return True
        else:
            logging.error(f'Falha ao baixar o arquivo. Status code: {resposta.status_code}')
            return False
    except Exception as e:
        logging.error(f'Erro ao baixar o arquivo: {e}')
        return False

# ---------------------------------------------------------------------------
def tratar_dados(diretorio_destino):
    """
    Lê o arquivo CSV, transforma os dados e adiciona novos campos.

    Parâmetros:
    diretorio_destino (Path): Caminho onde o arquivo CSV está localizado.

    Retorna:
    DataFrame: DataFrame com os dados transformados.
    """
    try:
        # Leitura do arquivo CSV
        df_people = pd.read_csv(diretorio_destino / "people.csv")
        logging.info(f"Arquivo CSV lido com sucesso. Total de {len(df_people)} linhas.")
        
        # Criar um novo campo "idade"
        ano_atual = datetime.now().year
        df_people["age"] = ano_atual - pd.to_datetime(df_people["Date of birth"]).dt.year
        
        # Renomear colunas
        rename_coluns = {
            "Index": "index",
            "User Id": "id",
            "First Name": "first_name",
            "Last Name": "last_name",
            "Sex": "gender",
            "Email": "email",
            "Phone": "phone",
            "Date of birth": "date_of_birth",
            "Job Title": "job_title",
            "age": "age"
        }

        df_people["generation"] = "Unknow"

        df_people.loc[(df_people["age"] >= 45) & (df_people["age"] <= 60), "generation"] = "gen x"
        df_people.loc[(df_people["age"] >= 29) & (df_people["age"] <= 44), "generation"] = "gen y"
        df_people.loc[(df_people["age"] >= 13) & (df_people["age"] <= 28), "generation"] = "gen z"

        df_people.rename(columns=rename_coluns, inplace=True)
        return df_people

    except Exception as e:
        logging.error(f'Erro ao tratar os dados: {e}')

# ---------------------------------------------------------------------------
def salvar_datraframe(diretorio_destino, df_people):
    """
    Salva o DataFrame transformado em um arquivo CSV no diretório de destino.

    Parâmetros:
    diretorio_destino (Path): Caminho onde o arquivo será salvo.
    df_people (DataFrame): DataFrame a ser salvo.
    """
    try:
        # Definindo o caminho do arquivo de saída
        arquivo_saida = diretorio_destino / "people_transformed.csv"

        # Salvando o DataFrame no arquivo CSV
        df_people.to_csv(arquivo_saida, index=False)
        logging.info(f"DataFrame salvo com sucesso em: {arquivo_saida}")
    except Exception as e:
        logging.error(f"Erro ao salvar o DataFrame: {e}")

# ---------------------------------------------------------------------------
def main():
    """
    Função principal que orquestra o fluxo de execução do script.
    """
    pasta = "people"
    diretorio_destino = criar_diretorio_destino(pasta)
    logging.info(f"Diretorio destino: {diretorio_destino}")

    if diretorio_destino:
        base_url = "https://drive.google.com/uc?id=1VEi-dnEh4RbBKa97fyl_Eenkvu2NC6ki&export=download"
        if baixar_csv(base_url, diretorio_destino):
            df_people = tratar_dados(diretorio_destino)
            if df_people is not None:
                salvar_datraframe(diretorio_destino, df_people)
            else:
                logging.error("Erro ao processar os dados.")
        else:
            logging.error('Falha ao baixar o arquivo.')
    else:
        logging.error('Falha ao criar o diretório de destino.')

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()