def input_idade():
    valida_idade = False
    idade = int(input('Digite idade: '))
    while not valida_idade:
        if idade < 1 or idade > 150:
            print('Dados invalidos!')
            idade = int(input('Digite idade: '))
        else:
            valida_idade = True


def input_nome():
    valida_nome = False
    nome = str(input('Digite nome: ')).strip().upper()
    while not valida_nome:
        if len(nome) < 3:
            print('Dados invalidos!')
            nome = str(input('Digite nome: ')).strip().upper()
        else:
            valida_nome = True


def input_salario():
    salario = float(input('Digite salario: '))
    while salario < 1:
        print('Dados invalidos!')
        salario = float(input('Digite salario: '))


def input_sexo():
    while True:
        resp = input("Sexo: [M/F] ").upper()[0]
        if resp in "MF":
            break
        print("ERRO! Digite apenas M ou F")


def input_estado_civil():
    while True:
        print("[S] Solteiro\n[C]Casado\n[V] Viuvo")
        estado_civil = input("Digite a sua opção SCV: ").upper()[0]
        if estado_civil in 'SCV':
            break
        print('Dados invalidos!')


input_nome()
input_idade()
input_sexo()
input_estado_civil()
input_salario()
