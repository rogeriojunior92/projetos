# Importar biblioteca e modulos
import os
import json
import requests
import pandas as pd
from pprint import pprint
from datetime import datetime

# ---------------------------------------------------------------------------------------------------------
# Função para manipular data/hora
def get_hour():
    data_now = datetime.now().strftime('%Y%m%d')
    return data_now

# ---------------------------------------------------------------------------------------------------------
# Função para criar diretório
def create_path(folder):
    try:
        BASE_PATH = os.path.dirname(__file__)
        BASE_FOLDER = os.path.join(BASE_PATH + f"/datalake/bronze/api/{folder}").replace("\\", "/")
        os.makedirs(BASE_FOLDER)
        print(f"#### BASE_FOLDER: {BASE_FOLDER}")
    except FileExistsError as er:
        print(f"\33[31m #### BASE_FOLDER {BASE_FOLDER} already exists.\33[m")

    return BASE_FOLDER

# ---------------------------------------------------------------------------------------------------------
# Função para consumir os dados API de Cotação
def get_currency():
    
    # https://docs.awesomeapi.com.br/api-de-moedas
    folder = 'moedas'
    folder = create_path(folder)

    with open(folder + "/lista_moedas.txt", 'r') as arquivo:

        print("\033[32mINICIANDO A EXTRAÇÃO DOS DADOS\33[m")

        request_dict = {}
        for linha in arquivo:

            dado = linha.replace("\n", "")
            headers = {'Content-type': 'application/json'}
            BASE_URL = f'https://economia.awesomeapi.com.br/json/last/{dado}'
            print(f"{BASE_URL}")
            request = requests.get(BASE_URL, headers=headers)
            request_dict[dado] = request.json()

        return request_dict

# ---------------------------------------------------------------------------------------------------------
# Função principal que executa todo o processo
def main():

    data = get_hour()
    folder = 'moedas'
    folder = create_path(folder)
    currency = get_currency()
    # print(f"Currency: {currency}")

    list_currency = []
    for chave in currency:
        for keys in currency[chave].values():
            try:
                code = keys['code']
                codein = keys['codein']
                name = keys['name']
                bid = keys['bid']
                create_date = keys['create_date']
            except:
                pass

            list_currency.append([code, codein, name, bid, create_date])
        
    df_currency = pd.DataFrame(list_currency, columns=['code', 'codein', 'name', 'bid', 'create_date'])
    df_currency.to_csv(folder + f"/currency_{data}.csv") 
    # df_currency.drop_duplicates()
    print(df_currency)

# ---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # Calling main() function
    main()