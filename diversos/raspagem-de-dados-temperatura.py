# Imports Libs
import os
import pandas as pd
from time import sleep
from datetime import datetime, timedelta

# Lista que contém as cidades
list_city = ['Boston', 'London', 'RioDeJaneiro', 'SaoPaulo']

key = "X889VXJMHKDT7HYEAP5L45MF9"

# Intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# Formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

# Criar pasta.
try:
    path = f"C:/Users/Dell/Documents/Eng/Projetos/venv/semana-{data_inicio}/"
    if not (os.path.exists(path)):
        os.mkdir(path)
        sleep(1)
    print("\033[32mPasta criada com sucesso\33[m")
except:
    sleep(1)
    print("\033[31mA pasta já existe e não pode ser criada.\033[m")
    
# Extração de dados da API weather.visualcrossing.com
# Ler o arquivo CSV
# Criar o arquivo CSV e concatenando com o diretório
sleep(1)
print("\033[34m ----------------- INICIANDO EXTRAÇÃO DOS DADOS ------------------\33[m")
for city in list_city:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv"
    sleep(1)
    print(f"------------------ EXTRAINDO DADOS \033[32m{city} ------------------\33[m")
    dados = pd.read_csv(url)
    print(dados.head())  
    dados.to_csv(path + f'dados_brutos_{city}.csv')
    sleep(1)
print("\033[32m ----------------- EXTRAÇÃO DOS DADOS FINALIZADO -----------------\33[m")
