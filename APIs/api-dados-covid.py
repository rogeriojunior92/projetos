import os
import sqlite3
import requests
from bs4 import BeautifulSoup

# -----------------------------------------------------------------------------------------------------------
# 1. Criar diretório
# 2. Raspagem dos dados / extrair os estados da página
# 3. Tratamento e limpeza dos dados
# 4. Extrair dados da API
# 5. Carregar os dados no banco de dados SQLite

# -----------------------------------------------------------------------------------------------------------
def extrair_estados(BASE_URL):

    """
    Extrai SIGLAS de uma página HTML.

    Args:
        base_url (str): URL da página da qual extrair as SIGLAS.

    Returns:
        list: Lista de ESTADOS extraídos.

    """

    lista_estados = list()

    try:
        request = requests.get(BASE_URL)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser') # Seleciona a tabela que contém os estados
            tabela = soup.find('div', class_='table-responsive') # Encontre o elemento que contém os nomes dos estados

            # Verifica se a tabela foi encontrada
            if tabela:
                linhas = tabela.find_all('tr') # Encontra todas as linhas da tabela
                # Iterar sobre cada linha da tabela, excluindo o cabeçalho
                for estado in linhas[1:]:
                    # Verificar se existem colunas suficientes na linha
                    colunas = estado.find_all('td')
                    # Verifica se há pelo menos 2 colunas (índices 0 e 1)
                    if len(colunas) >=2:
                        # Extrai o texto da segunda coluna (sigla do estado)
                        sigla_estado = colunas[1].text.strip() 
                        # Para cada célula, ele extrai o texto, removendo espaços em branco extras, e adiciona o estado à lista lista_estados
                        lista_estados.append(sigla_estado)

            # Retorna a lista de lista_estados
            return lista_estados

        else:
            print('Erro durante a conexão com a API.')

    except requests.RequestException  as e:
        print(f'Erro ao fazer a solicitação HTTP: {e}')

# -----------------------------------------------------------------------------------------------------------
def tratamento_estados(BASE_URL):

    """
    Altera a string SIGLA para minúscula.

    Args:
        base_url (str): URL da página da qual extrair os CNPJs.

    Returns:
        list: Lista das SIGLAS em minúscula.
    """

    estados = extrair_estados(BASE_URL)

    lista_estados = list()

    for lista in estados:
        nome_estado = lista.lower()
        lista_estados.append(nome_estado)

    return lista_estados

# -----------------------------------------------------------------------------------------------------------
def extrair_dados_estados(BASE_URL):

    """
    Extrai informações das SIGLAS de uma API pública.

    Args:
        base_url (str): URL base da API.

    Returns:
        dict: Dicionário contendo informações das SIGLAS.
    """

    lista_estados = tratamento_estados(BASE_URL)

    request_dict = dict()
    for lista in lista_estados:       
        try:
            BASE_URL_ESTADO = f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{lista}'
            request = requests.get(BASE_URL_ESTADO)
            if request.status_code == 200:
                request_dict[lista] = request.json()
            else:
                print('Erro durante a conexão com a API.')
        
        except requests.exceptions.RequestException as e:
            print(f'Erro durante a requisição da API: {e}')

    return request_dict

# -----------------------------------------------------------------------------------------------------------
def connection_db(database):

    """
    Estabelece uma conexão com o banco de dados SQLite.

    Args:
        database (str): Nome do diretório onde o banco de dados será criado.

    Returns:
        str: Caminho completo do banco de dados SQLite.
    """

    try:
        BASE_PATH = os.path.dirname(__file__)
        BASE_FOLDER = os.path.join(BASE_PATH + f'/cadastro/{database}.db')
        os.makedirs(BASE_FOLDER, exist_ok=True)
        print(f'{BASE_FOLDER} database criado com sucesso.')
    except FileExistsError:
        print(f'{BASE_FOLDER} database já existe.')

    return BASE_FOLDER

# -----------------------------------------------------------------------------------------------------------
def main():

    BASE_URL = 'https://mundoeducacao.uol.com.br/geografia/estados-brasil.htm'
    request_dict = extrair_dados_estados(BASE_URL)

    # Conectar ao banco de dados SQLite
    database = 'cadastro'
    PATH_DB = connection_db(database)
    conn = sqlite3.connect(PATH_DB)
    # Criar cursor
    cursor = conn.cursor()
    
    # Truncando a tabela antes de inserir novos registros
    sql_truncate = ("""TRUNCATE TABLE tb_estados""")
    cursor.execute(sql_truncate)
    conn.commit()

    # Criar a tabela, se caso não existir
    cursor.execute("""CREATE TABLE IF NOT EXISTS tb_estados(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   uid TEXT,
                   uf TEXT,
                   state TEXT,
                   cases FLOAT,
                   deaths FLOAT, 
                   suspects FLOAT,
                   refuses FLOAT,
                   datetime DATE 
                   )""")
    conn.commit()
    print('Tabela criada com sucesso.')

    # Inserir dados na tabela
    for valor in request_dict.values(): 
        try:
            uid = valor['uid']
            uf = valor['uf']
            state = valor['state']
            cases = valor['cases']
            deaths = valor['deaths']
            suspects = valor['suspects']
            refuses = valor['refuses']
            datetime = valor['datetime']

            cursor.execute("""INSERT INTO tb_estados(uid, uf, state, cases, deaths, suspects, refuses, datetime)
                              VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (uid, uf, state, cases, deaths, suspects, refuses, datetime))
                                
            print('Dados inseridos com sucesso')

        except Exception as e:
            print(f'Erro ao inserir registros no banco de dados: {e}')
    
    # Confirmar a transação
    conn.commit()

    # Fechar conexão com o banco de dados
    conn.close()

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()