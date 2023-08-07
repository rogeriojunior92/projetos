import os
import requests
import pandas as pd
from time import sleep
from datetime import datetime

# ---------------------------------------------------------------------------------------------------------
data_atual = datetime.now().strftime("%Y%m%d")

# ---------------------------------------------------------------------------------------------------------
try:
    BASE_PATH = os.path.dirname(__file__)
    BASE_PATH = os.path.join(BASE_PATH + "/datalake/bronze").replace("\\", "/")
    os.makedirs()
    print(f"BASE PATH: {BASE_PATH}")
except FileExistsError as er:
    print(f"\033[31mFolder {BASE_PATH} already exists.\33[m")

# ---------------------------------------------------------------------------------------------------------
BASE_URL = "https://brasilapi.com.br/api/cvm/corretoras/v1"
request = requests.get(BASE_URL)
request_dict = request.json()

dados = {"cnpj":[], "type":[], "nome_social":[], "nome_comercial":[], "status":[], "email":[],
         "telefone":[], "cep":[], "pais":[], "uf":[], "municipio":[], "bairro":[], "complemento":[],
         "logradouro":[], "data_patrimonio_liquido":[], "valor_patrimonio_liquido":[], "codigo_cvm":[],
         "data_inicio_situacao":[], "data_registro":[]}

try:
    if request.status_code == 200:
        print("Status OK")
        sleep(1)
        print("Inicio da Extração dos Dados")
        for requisicao in request_dict:
            cnpj = requisicao['cnpj']
            type = requisicao['type']
            nome_social = requisicao['nome_social']
            nome_comercial = requisicao['nome_comercial']
            status = requisicao['status']
            email = requisicao['email']
            telefone = requisicao['telefone']
            cep = requisicao['cep']
            pais = requisicao['pais']
            uf = requisicao['uf']
            municipio = requisicao['municipio']
            bairro = requisicao['bairro']
            complemento = requisicao['complemento']
            logradouro = requisicao['logradouro']
            data_patrimonio_liquido = requisicao['data_patrimonio_liquido']
            valor_patrimonio_liquido = requisicao['valor_patrimonio_liquido']
            codigo_cvm = requisicao['codigo_cvm']
            data_inicio_situacao = requisicao['data_inicio_situacao']
            data_registro = requisicao['data_registro']

            dados['cnpj'].append(cnpj)
            dados['type'].append(type)
            dados['nome_social'].append(nome_social)
            dados['nome_comercial'].append(nome_comercial)
            dados['status'].append(status)
            dados['email'].append(email)
            dados['telefone'].append(telefone)
            dados['cep'].append(cep)
            dados['pais'].append(pais)
            dados['uf'].append(uf)
            dados['municipio'].append(municipio)
            dados['bairro'].append(bairro)
            dados['complemento'].append(complemento)
            dados['logradouro'].append(logradouro)
            dados['data_patrimonio_liquido'].append(data_patrimonio_liquido)
            dados['valor_patrimonio_liquido'].append(valor_patrimonio_liquido)
            dados['codigo_cvm'].append(codigo_cvm)
            dados['data_inicio_situacao'].append(data_inicio_situacao)
            dados['data_registro'].append(data_registro)
except:
    print("Ocorreu um erro na conexão da API.")
    
sleep(1)
print("Dados Extraídos com sucesso")

# ---------------------------------------------------------------------------------------------------------
df_dados = pd.DataFrame(dados)
df_dados.info()
sleep(1)
print("Criando o DataFrame")
df_dados.to_csv(BASE_PATH + f"/dados_capital_{data_atual}.csv")
sleep(1)
print(f"DataFrame criado no diretório:\n{BASE_PATH + f'/dados_capital_{data_atual}'}")