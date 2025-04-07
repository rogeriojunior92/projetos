import os
import pandas as pd
from faker import Faker
from random import randint
from datetime import datetime

# ---------------------------------------------------------------------------------------------------------
# Manipulação de Data / Hora
def create_date():
    data_atual = datetime.now().strftime("%Y%m%d")
    return data_atual

data = create_date()

# ---------------------------------------------------------------------------------------------------------
# Manipulação dados Faker pt-BR
def definition_locality():
    locale = 'pt-BR'
    faker = Faker(locale)
    return faker

fakers = definition_locality()

# ---------------------------------------------------------------------------------------------------------
# Criar diretório, caso não exista.
def create_folder(folder):
    try:
        base_url  = os.path.dirname(__file__)
        base_path = os.path.join(base_url + f"/datalake/bronze/{folder}").replace("\\", "/")
        os.makedirs(base_path)
        print(f"Path: {base_path} criado com sucesso.")
    except FileExistsError as er:
        print(f"\033[31mFolder {base_path} already exists.\33[m")
    return base_path

# ---------------------------------------------------------------------------------------------------------
print("Extraíndo os dados Fake")
def create_register(lista_cadastro):
    for c in range(100):
        cadastro = {}
        cadastro['data'] = data
        cadastro['nome'] = fakers.name()
        cadastro['email'] = fakers.email()
        cadastro['telefone'] = fakers.phone_number()
        cadastro['trabalho'] = fakers.job()
        cadastro['ganho_por_hora'] = randint(1, 100)
        cadastro['horas_trabalhada_mes'] = randint(1, 168)
        cadastro['salario'] = cadastro['ganho_por_hora'] * cadastro['horas_trabalhada_mes']

        lista_cadastro.append(cadastro.copy())
        
print("Dados extraídos com sucesso")

# ---------------------------------------------------------------------------------------------------------
# Programa Principal
folder = 'cadastro'
lista_cadastro = list()

print("Criando o DataFrame")
def main():
    pasta = create_folder(folder)
    create_register(lista_cadastro)
    df_dados = pd.DataFrame(lista_cadastro, replace=True)
    df_dados.to_csv(pasta + str(f"/cadastro_{data}.csv"))
    print(df_dados)


if __name__ == '__main__':
    # Calling main() function
    main()