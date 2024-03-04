import re
from datetime import datetime

# -----------------------------------------------------------------------------------------------------------
# Função para criar o titulo
def titulo(txt):
    print('-' *50)
    print(txt)
    print('-' *50)

# -----------------------------------------------------------------------------------------------------------
# Função para obter o nome com validação
def obter_nome():

    while True:
        nome = input('Nome: ').title().strip()
        if nome.isalpha(): # Verifica se o nome contém apenas letras
            return nome
        else:
            print('\033[31mNome inválido. Por favor, insira um nome válido.\033[m')

# -----------------------------------------------------------------------------------------------------------
# Função para obter o e-mail com validação
def obter_email():

    while True:
        email = input('E-mail: ')
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return email
        else:
            print('\033[31mE-mail inválido. Por favor, insira um e-mail válido.\033[m')

# -----------------------------------------------------------------------------------------------------------
# Função para obter o sexo com validação
def obter_sexo():

    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo in "MF":
            return sexo
        elif sexo == "":
            print('\033[31mPor favor, insira M para masculino ou F para feminino.\033[m')
        else:
            print('\033[31mSexo inválido. Digite M para Masculino ou F para Feminino.\33[m')

# -----------------------------------------------------------------------------------------------------------
# Função para calcular a idade
def calcular_idade(ano_nasc):

    idade = datetime.now().year - ano_nasc
    return idade

# -----------------------------------------------------------------------------------------------------------
# Função para obter o telefone com validação
def obter_telefone():

    while True:
        telefone = input('Telefone (apenas números): ')
        if re.match(r'^\d{10,11}$', telefone):
            return telefone
        else:
            print('\033[31mTelefone inválido. Insira apenas números (10 ou 11 dígitos).\033[m')

# -----------------------------------------------------------------------------------------------------------
# Função para obter o departamento e calcular o salario
def obter_departamento(hora_trabalhada, hora_trabalhada_mes):

    while True:
        titulo('SELECIONE O DEPARTAMENTO'.center(50))
        print('0 - Sair\n1 - TI\n2 - Fiscal\n3 - RH')
        print('-' *50)
        opcao = int(input('Digite a opção: '))
        if opcao == 0:
            print('\033[32mSaindo do progrma...\33[m')
            return None, None
        elif opcao in [1, 2, 3]:
            if opcao == 1:
                departamento = "TI"
            elif opcao == 2:
                departamento = "Fiscal"
            elif opcao == 3:
                departamento = "RH"
        
            salario = hora_trabalhada * hora_trabalhada_mes
            return departamento, salario

        else:
            print('\033[31mOpção inválida. Digite um número entre 0 e 3.\033[m')

# -----------------------------------------------------------------------------------------------------------
# Função que executa todo o processo
def main():

    cadastro = dict()
    lista_cadastro = list()
    for c in range(2):
        titulo(f'{c+1}º CADASTRO'.center(50))
        cadastro['nome'] = obter_nome()
        cadastro['email'] = obter_email()
        cadastro['sexo'] = obter_sexo()
        cadastro['telefone'] = obter_telefone()
        cadastro['ano_nasc'] = int(input('Ano de Nascimento: '))
        cadastro['idade'] = calcular_idade(cadastro['ano_nasc'])
        hora_trabalhada = float(input('Digite o valor cobrado por hora: R$ '))
        hora_trabalhada_mes = int(input('Digite a quantidade de horas trabalhada no mês: '))
        departamento, salario = obter_departamento(hora_trabalhada, hora_trabalhada_mes)
        if departamento is not None and salario is not None:
                cadastro['departamento'] = departamento
                cadastro['salario'] = salario

        lista_cadastro.append(cadastro.copy())
        
    titulo('ANALISANDO A LISTA DE PESSOAS'.center(50))
    for lista in lista_cadastro:
        print(lista)
    print('-' *50)

# -----------------------------------------------------------------------------------------------------------
# Execução do programa
if __name__ == '__main__':
    main()