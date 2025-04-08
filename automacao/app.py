import os
import time
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -----------------------------------------------------------------------
# Carregar variáveis de ambiente
load_dotenv()

# -----------------------------------------------------------------------
# Configura o WebDriver para usar o Chrome
def configurar_driver():
    """Configura o WebDriver para usar o Chrome."""
    service = Service(GeckoDriverManager().install())
    options = Options()
    options.add_argument("-private")

    # Inicia o navegador
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    return driver

# -----------------------------------------------------------------------
def abrir_pagina(driver, url):
    # Acessa uma página
    driver.get(url)

# -----------------------------------------------------------------------
def inserir_usuario(driver):

    """Insere o usuário (e-mail) na página de login."""

    # Espera até o campo de texto do e-mail estar visível
    campo_texto_usuario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "i0116"))
    )

    # Pausa antes de digitar o usuário
    print("Esperando antes de inserir o usuário...")
    time.sleep(2)

    # Obtém o endereço de e-mail da variável de ambiente
    usuario = os.getenv("SEU_USUARIO")
    if usuario:
        campo_texto_usuario.send_keys(usuario)
    else:
        print("A variável de ambiente 'USER' não foi encontrada!")
        return False
    
    # Pausa após inserir o usuário
    print("Usuário inserido, esperando antes de pressionar Enter...")
    time.sleep(2)

    # Pressiona Enter após digitar o e-mail
    campo_texto_usuario.send_keys(Keys.RETURN)
    return True

# -----------------------------------------------------------------------
def inserir_senha(driver):
    
    """Insere a senha na página de login."""

    # Tenta localizar o campo de senha com dois IDs possíveis
    try:
        campo_texto_senha = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "i0118"))
        )
        print("Campo de senha encontrado com ID 'i0118'")
    except:
        campo_texto_senha = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='passwordEntry']"))
        )
        print("Campo de senha encontrado com XPath '//*[@id='passwordEntry']'")

    # Pausa antes de digitar a senha
    print("Esperando antes de inserir a senha...")
    time.sleep(2)

    # Obtém a senha da variável de ambiente
    senha = os.getenv("SUA_SENHA")
    if senha:
        campo_texto_senha.send_keys(senha)
    else:
        print("A variável de ambiente 'PASSWORD' não foi encontrada!")
        return False
    
    # Pausa após inserir a senha
    print("Senha inserida, esperando antes de pressionar Enter...")
    time.sleep(2)

    # Pressiona Enter após digitar a senha
    campo_texto_senha.send_keys(Keys.RETURN)
    return True

# -----------------------------------------------------------------------
def clicar_avancar(driver):

    """Clica no botão de avançar após inserir a senha."""

    # Espera até o botão 'Avançar' estar clicável (ajuste o ID conforme necessário)
    try:
        botao_avancar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "declineButton"))
        )
        print("Clicando no botão 'Avançar' com o ID 'declineButton'...")
        botao_avancar.click()
    except:
        # Se não encontrar o botão pelo ID, tenta pelo XPath
        try:
            botao_avancar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='view']/div/div[5]/button[2]"))
            )
            print("Clicando no botão 'Avançar' pelo XPath...")
            botao_avancar.click()
        except Exception as e:
            print(f"Erro ao tentar clicar no botão: {e}")

# -----------------------------------------------------------------------
def acessar_email(driver):

    """Função principala para realizar login."""

    if not inserir_usuario(driver):
        return  # Se falhar ao inserir o usuário, sai da função
    if not inserir_senha(driver):
        return  # Se falhar ao inserir a senha, sai da função
    clicar_avancar(driver)

# -----------------------------------------------------------------------
def main():
    
    """Função principal que executa todo o processo."""

    driver = configurar_driver()
    url = "http://outlook.office.com/owa"

    abrir_pagina(driver, url)
    acessar_email(driver)

# -----------------------------------------------------------------------
if __name__ == "__main__":
    main()