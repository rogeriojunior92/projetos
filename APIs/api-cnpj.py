import os
import re
import sqlite3
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# -----------------------------------------------------------------------------------------------------------
def criar_diretorio(folder):

    """
    Cria um diretório se ele não existir.

    Args:
        folder (str): Nome do diretório.

    Returns:
        str: Caminho completo do diretório criado.
    """

    try:
        BASE_PATH = os.path.dirname(__file__)
        BASE_FOLDER = os.path.join(BASE_PATH + f'/{folder}').replace('\\', '/')
        os.makedirs(BASE_FOLDER, exist_ok=True)
        print(f'{BASE_FOLDER} criado com sucesso.')
    except FileExistsError:
        print(f'{BASE_FOLDER} já existe.')

    return BASE_FOLDER

# -----------------------------------------------------------------------------------------------------------
def extrair_cnpj(headers, BASE_URL):

    """
    Extrai CNPJs de uma página HTML.

    Args:
        headers (dict): Cabeçalhos HTTP para a requisição.
        base_url (str): URL da página da qual extrair os CNPJs.

    Returns:
        list: Lista de CNPJs extraídos.

    """
    try:     
        request = requests.get(BASE_URL, headers=headers)
        # Lança uma exceção se a resposta não for bem-sucedida
        request.raise_for_status()
        soup = BeautifulSoup(request.content, 'html.parser')
        tabela = soup.find('table', class_='table-striped')

        lista_cnpjs = list()
        # Iterar sobre cada linha da tabela, excluindo o cabeçalho
        for linha in tabela.find_all('tr')[1:]:
            # Verificar se existem colunas suficientes na linha
            colunas = linha.find_all('td')
            # Verifica se há pelo menos 2 colunas (índices 0 e 1)
            if len(colunas) >= 2:
                # Extrair o CNPJ da segunda coluna (índice 1)
                cnpjs = colunas[1].text.strip()
                lista_cnpjs.append(cnpjs)
            else:
                print("Número insuficiente de colunas nesta linha.")
    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")
        
    return lista_cnpjs

# -----------------------------------------------------------------------------------------------------------
def limpeza_cnpjs(headers, BASE_URL):

    """
    Limpa os CNPJs removendo caracteres não numéricos.

    Args:
        headers (dict): Cabeçalhos HTTP para a requisição.
        base_url (str): URL da página da qual extrair os CNPJs.

    Returns:
        list: Lista de CNPJs limpos.
    """
    
    lista_cnpjs = extrair_cnpj(headers, BASE_URL)

    lista_cnpjs_limpos = list()

    for cnpj in lista_cnpjs:
        # Utilizando expressão regular para remover caracteres não numéricos
        cnpj_limpo = re.sub(r'\D', '', cnpj)
        lista_cnpjs_limpos.append(cnpj_limpo)
        
    return lista_cnpjs_limpos

# -----------------------------------------------------------------------------------------------------------
def extrair_dados_cnpj(headers, BASE_URL):

    """
    Extrai informações do CNPJ de uma API pública.

    Args:
        headers (dict): Cabeçalhos HTTP para a requisição.
        base_url (str): URL base da API.

    Returns:
        dict: Dicionário contendo informações do CNPJ.
    """
    
    lista_cnpjs_limpos = limpeza_cnpjs(headers, BASE_URL)

    request_dict = dict()
    try:
        for cnpj in lista_cnpjs_limpos:
            request_url  = f'https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}'
            request = requests.get(request_url , headers)
            request.raise_for_status()
            request_dict[cnpj] = request.json()
            print(request_dict)
    except requests.exceptions.RequestException as e:
        print(f'Erro durante a requisição da API: {e}')

    return request_dict

# -----------------------------------------------------------------------------------------------------------
# Função que abre a conexão com o banco de dados SQLite
def connection_sqlite(folder):

    """
    Estabelece uma conexão com o banco de dados SQLite.

    Args:
        folder (str): Nome do diretório onde o banco de dados será criado.

    Returns:
        str: Caminho completo do banco de dados SQLite.
    """

    path_db = folder + '/cadastro.db'
    return path_db

# -----------------------------------------------------------------------------------------------------------
# Função que executa todo o processo
def main():

    # Criar diretório
    folder = 'cadastro'
    folder = criar_diretorio(folder)

    # Configurar cabeçalhos e URL
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    BASE_URL = 'https://fateccampinas.com.br/conveniados/public/lista-empresa'

    # Extrair dados do CNPJ e API
    request_dict = extrair_dados_cnpj(headers, BASE_URL)

    # Conectar ao banco de dados SQLite
    path_db = connection_sqlite(folder)
    conn = sqlite3.connect(path_db)

    # Criar cursor
    cursor = conn.cursor()

    # Criar a tabela, se caso não existir
    cursor.execute("""CREATE TABLE IF NOT EXISTS empresas(
                    id PRIMARY KEY AUTOINCREMENT,
                    nome_fantasia TEXT,
                    razao_social TEXT,
                    status TEXT,
                    cnae_principal_descricao TEXT,
                    cnae_principal_codigo INTEGER,
                    cep TEXT,
                    data_abertura DATE,
                    ddd INTEGER,
                    telefone INTEGER,
                    email TEXT,
                    logradouro TEXT,
                    numero INTEGER,
                    complemento TEXT,
                    bairro TEXT,
                    municipio TEXT,
                    uf TEXT
                   )""")
    
    # Inserir dados na tabela
    for cnpj, dados in request_dict.items():
        try:
            nome_fantasia = dados.get['nome_fantasia', None]
            razao_social = dados.get['razao_social', None]
            status = dados['status', None]
            cnae_principal_descricao = dados.get['cnae_principal_descricao', None]
            cnae_principal_codigo = dados.get['cnae_principal_codigo', None]
            cep = dados.get['cep', None]
            data_abertura = dados.get['data_abertura', None]
            ddd = dados.get['ddd', None]
            telefone = dados.get['telefone', None]
            email = dados.get['email', None]
            logradouro = dados.get['logradouro', None]
            numero = dados.get['numero', None]
            complemento = dados.get['complemento', None]
            bairro = dados.get['bairro', None]
            municipio = dados.get['municipio', None]
            uf = dados.get['uf', None]

            cursor.execute("""INSERT INTO empresas(cnpj, nome_fantasia, razao_social, status, cnae_principal_descricao, cnae_principal_codigo, cep, telefone, data_abertura, 
                                                   ddd, telefone, email, logradouro, numero, complemento, bairro, municipio, uf)
                              VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (cnpj, nome_fantasia, razao_social, status, cnae_principal_descricao, cnae_principal_codigo, cep, telefone, data_abertura, 
                                                   ddd, telefone, email, logradouro, numero, complemento, bairro, municipio, uf))
                                                   
            print(f'Dados para CNPJ {cnpj} inseridos com sucesso.')

        except Exception as e:
            print(f'Erro ao inserir dados para CNPJ {cnpj}: {e}')

    # Confirmar a transação
    conn.commit()

    # Fechar conexão com o banco de dados
    conn.close()

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()