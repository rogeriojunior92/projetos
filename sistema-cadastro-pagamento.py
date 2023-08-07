import os
import pandas as pd
from faker import Faker
from datetime import datetime
from random import randint

locale = 'pt-BR'
faker = Faker(locale)

# ---------------------------------------------------------------------------------------------------------
# Função para manipular data/hora
def data_atual():
    data = datetime.now().strftime("%Y%m%d")
    return data

# ---------------------------------------------------------------------------------------------------------
# Função para criar diretório
def criar_diretorio(folder):
    try:
        BASE_PATH = os.path.dirname(__file__)
        BASE_FILE = os.path.join(BASE_PATH + f"/datalake/bronze/{folder}").replace("\\", "/")
        os.makedirs(BASE_FILE)
        print(f"Path: {BASE_FILE} criado com sucesso.")
    except FileExistsError as er:
        print(f"\033[31mFolder {BASE_FILE} already exists.\33[m")   
    
    return BASE_FILE

# ---------------------------------------------------------------------------------------------------------
# Função para calcular o salário
def calculo_salario(horas_trabalhadas, horas_trabalhadas_mes):
    salario = horas_trabalhadas * horas_trabalhadas_mes
    return salario

# ---------------------------------------------------------------------------------------------------------
# Função para calcular os descontos
def desconto_salario(salario):
    ir = salario * 5/100
    inss = salario * 10/100
    fgts = salario * 11/100
    total_desc = salario - ir - inss - fgts
    return total_desc

# ---------------------------------------------------------------------------------------------------------
# Programa Principal
print("-" *50)
print("FOLHA DE PAGAMENTO".center(50))
print("-" *50)
lista_cadastro = []

if __name__ == '__main__':
    for c in range(50):

        nome = faker.name()
        email = faker.email()
        trabalho = faker.job()
        horas_trabalhadas = randint(1, 68)
        horas_trabalhadas_mes = randint(1, 100)
        folder = 'calculo'
        data = data_atual()
        salario = calculo_salario(horas_trabalhadas, horas_trabalhadas_mes)
        total_desc = desconto_salario(salario)
        folder = criar_diretorio(folder)
        lista_cadastro.append([nome, email, trabalho, horas_trabalhadas, horas_trabalhadas_mes, salario])

    df_calculo = pd.DataFrame(lista_cadastro, columns=['nome', 'email', 'trabalho', 'horas_trabalhadas', 
                                                       'horas_trabalhadas_mes', 'salario'])
    df_calculo.to_csv(folder + f"/calculo_{data}.csv")

print("-" *50)