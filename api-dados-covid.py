import os
import requests
import pandas as pd
from datetime import datetime

# ---------------------------------------------------------------------------------------------------------
def get_data():

    data = datetime.now().strftime('%Y%m%d')
    return data

# ---------------------------------------------------------------------------------------------------------
def create_folder(folder):
    try:
        BASE_PATH = os.path.dirname(__file__)
        BASE_FOLDER = os.path.join(BASE_PATH + f"/datalake/bronze/api/{folder}").replace("\\", "/")
        os.makedirs(BASE_FOLDER)
        print(f"BASE_FOLDER: {BASE_FOLDER}")
    except FileExistsError as er:
        print(f"\33[31m #### BASE_FOLDER {BASE_FOLDER} already exists.\33[m")

    return BASE_FOLDER

# ---------------------------------------------------------------------------------------------------------
def get_data_covid():

    folder = 'dados_covid_estado'
    folder = create_folder(folder)

    print()
    request_dict = {}
    with open(folder + "/covid_estados.txt", "r") as arquivo:

        for file in arquivo:
            dado = file.replace("\n", "")
            headers = {'Content-type': 'application/json'}
            BASE_URL = f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{dado}'
            print(BASE_URL)
            request = requests.get(BASE_URL, headers=headers)
            request_dict[dado] = request.json()

        return request_dict
    
# ---------------------------------------------------------------------------------------------------------
def main():
    print()
    data = get_data()
    folder = 'dados_covid_estado'
    folder = create_folder(folder)
    dados = get_data_covid()
    print()
    print("\033[32mINICIANDO A EXTRAÇÂO DOS DADOS\33[m")

    lista_dados_covid = []
    for dado in dados.values():

        uid = dado['uid']
        uf = dado['uf']
        state = dado['state']
        cases = dado['cases']
        deaths = dado['deaths']
        suspects = dado['suspects']
        refuses = dado['refuses']
        date = dado['datetime']
    
        lista_dados_covid.append([uid, uf, state, cases, deaths, suspects, refuses, date])

    df_covid = pd.DataFrame(lista_dados_covid, columns=['uid', 'uf', 'state', 'cases', 'deaths', 'suspects', 'refuses', 'date'])
    df_covid.to_csv(folder + f"/dados_covid_{data}.csv")
    print(df_covid)

# ---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()