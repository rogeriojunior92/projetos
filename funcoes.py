# Função para criar linha
def linha():
    print("\033[34m-\33[m" *50)


# Função para criar linha e texto
def titulo(txt):
    print("\033[34m-\33[m" *50)
    print("\033[34m"+txt+"\33[m")
    print("\033[34m-\33[m" *50)


# Função para validar número inteiro ou interrupção pelo teclado
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(TypeError, ValueError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num
        

# Função para validar número ponto flutuate ou interrupção pelo teclado
def leiaFloat(msg):
    while True:
        try:
            num = int(input(msg))
        except(TypeError, ValueError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num


def menu(lista):
    titulo("CADASTRO DE FUNCIONÁARIOS".center(50))
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c +=1
    linha()
    opcao = leiaInt("Digite a sua opção: ")
    return opcao    