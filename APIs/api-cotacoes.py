# -----------------------------------------------------------------------------------------------------------
""" Importações de bibliotecas """

import os # Para operações de sistema
import re # Para expressões regulares,
import logging # Para registrar mensagens de informações, avisos e erros.
import requests # Para fazer solicitações HTTP
import pandas as pd # Trabalhar com dados em formato de DataFrame
from time import sleep # Permite suspender a execução do programa
from datetime import datetime # Para manipulação de datas e horários

# -----------------------------------------------------------------------------------------------------------
def criar_diretorio(folder):

    """Esta função cria um diretório se ele não existir. Ela recebe o nome do diretório como argumento e retorna o caminho para o diretório criado.."""

    try:
        BASE_PATH = os.path.dirname(__file__)
        BASE_FOLDER = os.path.join(BASE_PATH + f'/datalake/bronze/api/awesomeapi/{folder}').replace('\\', '/')
        os.makedirs(BASE_FOLDER, exist_ok=True)
        logging.info(f'{BASE_FOLDER} criado com sucesso.')
    except FileExistsError:
        logging.info(f'{BASE_FOLDER} já existe.')
    
    return BASE_FOLDER

# -----------------------------------------------------------------------------------------------------------
def extrair_moedas(folder):

    """Esta função extrai as moedas da API fornecida, armazena os dados em um arquivo de texto e imprime uma mensagem indicando se a extração foi bem-sucedida ou não."""

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    BASE_URL = 'https://economia.awesomeapi.com.br/xml/available'
    
    retries = 3 # Número de tentativas
    for i in range(retries):
        try:

            request = requests.get(BASE_URL, headers=headers)
            request.raise_for_status # Lança uma exceção se a solicitação não for bem-sucedida
            with open(folder + '/moedas.txt', "wt+", encoding='utf-8') as arquivo:
                arquivo.write(request.text)
            logging.info('Extração das moedas concluído com sucesso.')
            return # Sair da função após o sucesso
        
        except requests.exceptions.RequestException as e:
            logging.error(f'Erro ao fazer a solicitação: {e}')
        sleep(1)
    logging.error('Número máximo de tentativas excedido.')

# -----------------------------------------------------------------------------------------------------------
def limpeza_dados_moedas(folder):

    """Esta função lê os dados do arquivo de moedas, limpa-os usando expressões regulares e retorna uma lista de moedas."""

    lista_moedas = list()

    with open(folder + '/moedas.txt', "r") as xml_data:
       
        data = xml_data.read() # Lendo os dados do arquivo     
        patter = r'<([^/]+)>'
        matches = re.findall(patter, data)
        lista_moedas = matches[1:]  # Ignora a primeira moeda "?xml version..."

    return lista_moedas

# -----------------------------------------------------------------------------------------------------------
def leitura_moedas(folder):

    """Esta função lê as informações das moedas da API para cada moeda da lista limpa e retorna um dicionário contendo essas informações."""

    limpeza = limpeza_dados_moedas(folder)

    request_dict = dict()
    for dado in limpeza:
        headers = {'Content-type': 'application/json'}
        BASE_URL = f'http://economia.awesomeapi.com.br/json/last/{dado}'

        retries = 3 # Número de tentativas
        for i in range(retries):
            try:

                request = requests.get(BASE_URL, headers=headers)
                request.raise_for_status() # Lança uma exceção se a solicitação não for bem-sucedida
                request_dict[dado] = request.json()
                break # Se a solicitação for bem-sucedida, saia do loop de tentativas
            
            except requests.exceptions.ConnectionError as e:
                print(f'Erro de conexão: {e}')
            sleep(1) # Espera antes de tentar novamente

    return request_dict

# -----------------------------------------------------------------------------------------------------------
def criar_dataframe(lista_moedas):

    """Esta função cria um DataFrame do pandas a partir da lista de moedas fornecida e retorna o DataFrame."""

    lista_colunas = ['code', 'codein', 'name', 'bid', 'create_date']
    df_moedas = pd.DataFrame(lista_moedas, columns = lista_colunas)
    return df_moedas

# -----------------------------------------------------------------------------------------------------------
def main():

    """Esta é a função principal. Ela executa todo o processo: 
        - cria o diretório, 
        - lê as moedas, 
        - cria o DataFrame, 
        - converte-o em CSV 
        - imprime a saída.
    """

    folder = 'moedas'
    list_currency = list()
    folder = criar_diretorio(folder)
    request_dict = leitura_moedas(folder)
    
    for chave in request_dict:
        for keys in request_dict[chave].values():

            code = keys['code']
            codein = keys['codein']
            name = keys['name']
            bid = keys['bid']
            create_date = keys['create_date']

            list_currency.append([code, codein, name, bid, create_date])

    df_moedas = criar_dataframe(list_currency)
    filename = folder + f'/moedas_{datetime.now().strftime("%Y-%m-%d")}.csv'
    df_moedas.to_csv(filename, index=False)
    logging.info(f'Arquivo CSV salvo em: {filename}')

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()