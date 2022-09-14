import os
from datetime import datetime
from time import sleep

"""
Formula: Peso / (Altura x Altura)
"""
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


def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


def imc_masculino():
    os.system("cls")
    
    """
    Veja a interpretação do IMC - Masculino
    IMC 	            Categoria
    Abaixo de 20,7 	    Abaixo do peso
    20,7 a 26,4 	    Peso ideal
    26,5 a 27,8 	    Pouco acima do peso
    27,9 a 31,1 	    Acima do peso
    31,2 e acima 	    Obesidade
    """

    nome = input("Nome: ")
    ano_nascimnento = int(input("Ano de Nascimento: "))
    idade = datetime.now().year - ano_nascimnento
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    imc = peso / altura**2

    titulo("COLETANDO OS DADOS".center(50))
    sleep(0.5)
    print(f"Nome: {nome}\nIdade: {idade}\nPeso: {peso:.2f}Kg\nAltura: {altura:.2f}\nIMC: {imc:.2f} - ", end='')
    
    if imc < 20.7:
        print("Abaixo do peso")
    elif imc <= 20.7 and imc < 26.4:
        print("Peso ideal")
    elif imc <= 26.5 and imc < 27.8:
        print("Pouco acima do peso")
    elif imc <= 27.9 and imc < 31.1:
        print("Acima do peso")
    else:
        print("Obesidade")
    print("\033[1;94m-\033[0;0m" *50)
    os.system("pause")


def imc_feminino():
    os.system("cls")

    """
    Veja a interpretação do IMC - Feminino
    IMC                 Categoria
    Abaixo de 19,1   	Abaixo do peso
    19,1 a 25,8 	    Peso ideal
    25,9 a 27,3 	    Pouco acima do peso
    27,4 a 32,3 	    Acima do peso
    32,4 e acima     	Obesidade
    """
    
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de Nascimento: "))
    idade = datetime.now().year - ano_nascimento
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    imc = peso / altura ** 2

    titulo("COLETANDO OS DADOS".center(50))
    sleep(0.5)
    print(f"Nome: {nome}\nIdade: {idade}\nPeso: {peso:.2f}Kg\nAltura: {altura:.2f}\nIMC: {imc:.2f} - ", end='')
    
    if imc < 19.1:
        print("Abaixo do peso")
    elif imc <= 19.1 and imc < 25.8:
        print("Peso ideal")
    elif imc <= 25.9 and imc < 27.3:
        print("Pouco acima do peso")
    elif imc <= 27.4 and imc < 32.3:
        print("Acima do peso")
    else:
        print("Obesidade")
    print("\033[1;94m-\033[0;0m" *50)    
    os.system("pause")


def imc_idoso():
    os.system("cls")

    """
    Veja a interpretação do IMC - Idoso
    IMC 	             Categoria
    Até 22               Magreza
    22 a 27              Eutrofia (peso ideal)
    Acima 27             Obesidade
    """

    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de Nascimento: "))
    idade = datetime.now().year - ano_nascimento
    peso = float("Peso: ")
    altura = float("Altura: ")
    imc = peso / altura ** 2
    
    titulo("COLETANDO OS DADOS".center(50))
    sleep(0.5)
    print(f"Nome: {nome}\nIdade: {idade}\nPeso: {peso:.2f}Kg\nAltura: {altura:.2f}\nIMC: {imc:.2f} - ", end='')

    if imc < 22:
        print("Magreza")
    elif imc <= 22 and imc <= 27:
        print("Eutrofia (peso ideal)")
    else:
        print("Obesidade")
    print("\033[1;94m-\033[0;0m" *50)   
    os.system("pause")


def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA CALCULADORA DE IMC".center(50))
        print("1 - MASCULINO\n2 - FEMININO\n3 - IDOSO\n0 - SAIR")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            imc_masculino()
        elif opcao == 2:
            imc_feminino()
        elif opcao == 3:
            imc_idoso()
        elif opcao == 0:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 4\33[m")


menu()
