# Importar bibliotecas
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

print()
product = input("O que deseja buscar? ").title().strip()
while product == "":
    print("\033[31mDados Inválido.\33[m")
    product = input("O que deseja pesquisar? ").title().strip()

# Definição das instâncias de Driver
options = Options()
options.add_argument('--start-maximized')
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("detach", True)

# Atualização do webdriver manager de forma autómatica, sendo compatível com a versão atual do navegador.
servico = Service(ChromeDriverManager().install())
servico.start()

# Metodo
navegador = webdriver.Chrome(service=servico, options=options)
navegador.get("https://mercadolivre.com.br/")
navegador.find_element('xpath', '//*[@id="cb1-edit"]').send_keys(product)
print("\033[32mConnection established.\33[m")
sleep(5)
navegador.find_element('xpath', '/html/body/div[2]/div[1]/div/div[3]/button[1]').click() # Aceitar cookies
sleep(1)
navegador.find_element('xpath', '/html/body/header/div/div[2]/form/button/div').click() # Clicar no botão procurar

dict_final = {"produto": [], "preco": [], "url":[]}

print("\033[32m----- Starting ETL WebScraping -----\33[m")
c = 0
# Loop infinito para raspagem de cada página
while True:
    # Iteração com o layout de cada aparelho
    for iphone in navegador.find_elements('xpath', '//li[@class="ui-search-layout__item shops__layout-item"]'): # Obtém o layout de cada aparelho
        # for column in iphone.find_elements(By.TAG_NAME, 'li'):
        all_text_iphone = iphone.find_element('xpath', './/h2[@class="ui-search-item__title shops__item-title"]') # Obtém o titulo do aparelho
        all_text_price = iphone.find_element('xpath', './/span[@class="price-tag-fraction"]') # Obtém o preço do aparelho
        all_text_url = iphone.find_element('xpath', './/a[@class="ui-search-link"]').get_attribute("href") # Obtém a URL do aparelho
        # print(all_text_url)

        dict_final['produto'].append(all_text_iphone.text)
        dict_final['preco'].append(all_text_price.text)
        dict_final['url'].append(all_text_url)
        
    try:
        next_page = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Seguinte')))
        next_page.click()
        # navegador.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[9]/ul/li[3]/a/span[1]'))))
        # navegador.find_element('xpath', '//*[@id="root-app"]/div/div[2]/section/div[9]/ul/li[3]/a/span[1]').click()
        print(f"\033[32mNavigating to Next Page {c+1}\33[m")
        c+=1
    except:
        print("\033[31mLast page reached\33[m")
        break

sleep(10)
executionName = 'webscraping_ML'
print("\033[32mETL finished.\33[m")
print("\033[32mInitialed create dataframe...\33[m")
print("\033[32mDataframe created.\33[m")
print()
df_iphone = pd.DataFrame(dict_final, columns=['produto', 'preco', 'url'])
print(df_iphone)
df_iphone.to_csv(f"C:/Users/Dell/Documents/Eng/Projetos/venv/{executionName}.csv", encoding='utf-8', sep=';')