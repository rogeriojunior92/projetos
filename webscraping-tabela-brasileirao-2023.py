# Imports Libs
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Definição das instâncias de Driver
chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

# Verifica se há uma nova atualização do navegador Google Chrome
servico = Service(ChromeDriverManager().install())
servico.start()

# URL Tabela Brasileirão 2023
url = "https://www.google.com/search?client=firefox-b-d&q=tabela+brasileirao#sie=lg;/g/11jspy1hvm;2;/m/0fnk7q;st;fp;1;;;"
navegador = webdriver.Chrome(service=servico, options=chromeOptions)
navegador.get(url)
print("\033[32mConnection URL established.\33[m")
sleep(5)

# Dicionário com listas para armazenar os dados
dict_times = {"clube":[],
              "pontos":[],
              "partidas_jogadas":[],
              "vitorias":[],
              "empates":[],
              "derrotas":[],
              "gols_marcados":[],
              "gols_contra":[],
              "saldo_gols":[]
            }

print("####### STARTING DATA EXTRACTION #######")
# Iteração com a tabela da URLs
for time in navegador.find_elements('xpath', 
                                    '//*[@id="liveresults-sports-immersive__league-fullpage"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/table//tr'):
    # for column in time.find_elements(By.TAG_NAME, 'td'):
    all_times = time.find_elements(By.TAG_NAME, 'td')
    
    if all_times != []:
        dict_times["clube"].append(all_times[2].text)
        dict_times["pontos"].append(all_times[3].text)
        dict_times["partidas_jogadas"].append(all_times[4].text)
        dict_times["vitorias"].append(all_times[5].text)
        dict_times["empates"].append(all_times[6].text)
        dict_times["derrotas"].append(all_times[7].text)
        dict_times["gols_marcados"].append(all_times[8].text)
        dict_times["gols_contra"].append(all_times[9].text)
        dict_times["saldo_gols"].append(all_times[10].text)

#print(dict_times)
print("\033[32mExtraction data finished.33[m")

#==============================================================================================================
# Função principal que executa todo o processo
#==============================================================================================================
def main():
    print("\033[32mDataFrame create successful.\33[m")
    # Criando DataFrame para visualização dos dados de forma tabular
    df_times = pd.DataFrame(dict_times)
    print(df_times)

main()