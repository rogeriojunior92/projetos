import os
import re
import math
import requests
import pandas as pd
from bs4 import BeautifulSoup

dic_produtos = {'marca':[], 'preco':[]}

# URL para extração dos dados
url = "https://www.kabum.com.br/tv/tv-4k/50-polegadas"
# My User Agent do navegador
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}

site = requests.get(url, headers=headers) # Requisição ao URL
soup = BeautifulSoup(site.content, 'html.parser')
qtde_itens = soup.find('div', id='listingCount').get_text().strip()

index = qtde_itens.find(' ') # Variável para encontrar espaço vazio
qtde = qtde_itens[:index] # Variável para pegar o primeiro até o primeiro espaço
ultima_pag = math.ceil(int(qtde)/2) # Variável, utilizando lib math.ceil para arredondamento do número

#Iteração, irá percorrer todas as páginas e encontrar todos os produtos com a TAG 'productCard'
for i in range(1, ultima_pag+1):
    page = f'https://www.kabum.com.br/tv/tv-4k/50-polegadas?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(page, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))

    #Iteração, irá percorrer todos os produtos e retornará com a 'marca/modelo' e 'preço'
    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()

        print(marca, preco)

        # Armazenará os dados no dicionário com lista
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

    # Imprimi as páginas da iteração do primeiro laço de repetição
    print(page)

print('-' *40)
filename = 'raspagem_dados'
df = pd.DataFrame(dic_produtos)
df.to_csv(f'{os.getenv["USERPROFILE"]}\\Downloads\\{filename}.csv', encoding='utf-8', sep=';')
print("Arquivo criado com sucesso.")
