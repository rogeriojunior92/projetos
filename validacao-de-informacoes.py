import re

# Validações de dados

def input_idade():
    valida_idade = False
    idade = int(input('Digite idade: '))
    while not valida_idade:
        if idade < 1 or idade > 150:
            print('\033[31mDados invalidos!\33[m')
            idade = int(input('Digite idade: '))
        else:
            valida_idade = True


def input_nome():
    valida_nome = False
    nome = str(input('Digite nome: ')).strip().upper()
    while not valida_nome:
        if len(nome) < 3:
            print('\033[31mDados invalidos!\33[m')
            nome = str(input('Digite nome: ')).strip().upper()
        else:
            valida_nome = True


def input_salario():
    salario = float(input('Digite salario: '))
    while salario < 1:
        print('\033[31mDados invalidos!\33[m')
        salario = float(input('Digite salario: '))


def input_sexo():
    while True:
        resp = input("Sexo: [M/F] ").upper()[0]
        if resp in "MF":
            break
        print("\033[31mERRO! Digite apenas M ou F.\33[m")


def input_estado_civil():
    while True:
        print("[S] Solteiro\n[C]Casado\n[V] Viuvo")
        estado_civil = input("Digite a sua opção SCV: ").upper()[0]
        if estado_civil in 'SCV':
            break
        print('\033[31mDados invalidos!\33[m')


def valida_email():
    agenda = {}
    while True:
        agenda['email'] = input("E-mail: ")
        padrao = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(padrao, agenda['email']):
            print("\033[32mE-mail Válido.\33[m")
            break
        else:
            print("\033[31mE-mail Inválido.\33[m")


def valida_telefone():
    agenda = {}
    while True:
        try:
            agenda['telefone'] = input("Telefone (DD+numero): ")
            padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            resposta = re.search(padrao, agenda['telefone'])
            agenda["telefone"] = f'({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
            break
        except AttributeError:
            print("\033[31mDados Inválidos.\33[m")


input_nome()
input_idade()
input_sexo()
input_estado_civil()
input_salario()
valida_email()
valida_telefone()