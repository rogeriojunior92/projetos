import os
from time import sleep

def titulo(txt):
    print("\033[34m-\033[0;0m" *35)
    print('\033[34m'+txt+'\033[0;0m')
    print("\033[34m-\033[0;0m" *35)

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num

# Função para calcular a soma entre dois números
def somar(n1, n2):
    os.system("cls")
    total = n1 + n2
    sleep(0.5)
    print(f"Resultado: {n1} + {n2} = {total}")
    os.system("pause")

# Função para calcular a subtração entre dois números
def subtrair(n1, n2):
    os.system("cls")
    total = n1 - n2
    sleep(0.5)
    print(f"Resultado: {n1} - {n2} = {total}")
    os.system("pause")

# Função para calcular a multiplicação entre dois números
def multiplicar(n1, n2):
    os.system("cls")
    total = n1 * n2
    sleep(0.5)
    print(f"Resultado: {n1} x {n2} = {total}")
    os.system("pause")

# Função para calcular a divisão entre dois números
def dividir(n1, n2):
    os.system("cls")
    total = n1 / n2
    sleep(0.5)
    print(f"Resultado: {n1} ÷ {n2} = {total}")
    os.system("pause")     


def menu():
    while True:
        titulo("CALCULADORA PYTHON".center(35))
        print("[1] SOMAR\n[2] SUBTRAIR\n[3] MULTIPLICAR\n[4] DIVIDIR\n[5] SAIR")
        print("\033[34m-\033[0;0m" *35)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            somar(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")))
        elif opcao == 2:
            subtrair(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")))
        elif opcao == 3:
            multiplicar(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")))
        elif opcao == 4:
            dividir(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")))
        elif opcao == 5:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 8!\33[m")

menu()
