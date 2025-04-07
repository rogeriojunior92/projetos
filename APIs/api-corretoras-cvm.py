import os
import requests
import pandas as pd
from datetime import datetime

# ---------------------------------------------------------------------------------------------------------
def data_atual():
    now = datetime.now().strftime("%Y%m%d")
    return now

# ---------------------------------------------------------------------------------------------------------
def criar_diretorio(folder):
    try:
        BASE_PATH = os.path.dirname(__file__)
        BASE_FOLDER = os.path.join(BASE_PATH + f"/datalake/bronze/{folder}").replace("\\", "/")
        os.makedirs(BASE_FOLDER)
        print(f"PATH: {BASE_FOLDER} created success.")
    except FileExistsError as er:
        print(f"\033[31mFolder {BASE_FOLDER} already exists.\33[m") 

    return BASE_FOLDER

# ---------------------------------------------------------------------------------------------------------
def busca_dados(BASE_URL):
    
    request = requests.get(BASE_URL)
    request_dict = request.json()   
    return request_dict

# ---------------------------------------------------------------------------------------------------------
def main():

    dados_dict = {"cnpj":[], "type":[], "nome_social":[], "nome_comercial":[], "status":[], "email":[],
            "telefone":[], "cep":[], "pais":[], "uf":[], "municipio":[], "bairro":[], "complemento":[],
            "logradouro":[], "data_patrimonio_liquido":[], "valor_patrimonio_liquido":[], "codigo_cvm":[],
            "data_inicio_situacao":[], "data_registro":[]}


    BASE_URL = "https://brasilapi.com.br/api/cvm/corretoras/v1"
    dados = busca_dados(BASE_URL)

    for requisicao in dados:          
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

        dados_dict['cnpj'].append(cnpj)
        dados_dict['type'].append(type)
        dados_dict['nome_social'].append(nome_social)
        dados_dict['nome_comercial'].append(nome_comercial)
        dados_dict['status'].append(status)
        dados_dict['email'].append(email)
        dados_dict['telefone'].append(telefone)
        dados_dict['cep'].append(cep)
        dados_dict['pais'].append(pais)
        dados_dict['uf'].append(uf)
        dados_dict['municipio'].append(municipio)
        dados_dict['bairro'].append(bairro)
        dados_dict['complemento'].append(complemento)
        dados_dict['logradouro'].append(logradouro)
        dados_dict['data_patrimonio_liquido'].append(data_patrimonio_liquido)
        dados_dict['valor_patrimonio_liquido'].append(valor_patrimonio_liquido)
        dados_dict['codigo_cvm'].append(codigo_cvm)
        dados_dict['data_inicio_situacao'].append(data_inicio_situacao)
        dados_dict['data_registro'].append(data_registro)  
    
    data = data_atual()
    folder = 'dados_capital'
    pasta = criar_diretorio(folder)
    df_dados = pd.DataFrame(dados_dict)
    df_dados.info()
    df_dados.to_csv(pasta + f"/dados_capital_{data}.csv")


# ---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    print("DataFrame criado com sucesso.")