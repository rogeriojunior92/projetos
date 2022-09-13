import os
from random import randint
from time import sleep

itens = ["Pedra", "Papel", "Tesoura"]

computador = randint(0, 2)


def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


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


def menu():
    os.system("cls")
    
    empate = jogador_venceu = computador_venceu = 0

    while True:
        titulo("VAMOS JOGAR JO-KEN-PÔ".center(50))
        print("0 - PEDRA\n1 - PAPEL\n2 - TESOURA")
        print("\033[1;94m-\033[0;0m" *50)

        jogador = leiaInt("Escolha a sua jogada: ")
        print("\033[1;94m-\033[0;0m" *50)

        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PÔ")

        print("\033[1;94m-\033[0;0m" *50)
        print(f"Computador escolheu: {itens[computador]}")
        print(f"Jogador escolheu: {itens[jogador]}")
        print("\033[1;94m-\033[0;0m" *50)

        if computador == 0: # Computador escolheu PEDRA
            if jogador == 0:  # Jogador escolheu PEDRA
                print("EMPATE")
                empate += 1

            elif jogador == 1: # Jogador escolheu PAPEL
                print("JOGADOR GANHOU")
                jogador_venceu +=1

            elif jogador == 2: # Jogador escolhe TESOURA
                print("COMPUTADOR GANHOU")
                computador_venceu +=1

            else:
                print("\033[31mOpção inválida. Digite entre 1 e 3\33[m")

        elif computador == 1: # Computador escolheu PAPEL
            if jogador == 0:  # Jogador escolheu PEDRA
                print("COMPUTADOR GANHOU")
                computador_venceu +=1

            elif jogador == 1:  # Jogador escolheu PAPEL
                print("EMPATE")
                empate += 1

            elif jogador == 2:  # Jogador escolheu TESOURA
                print("JOGADOR GANHOU")
                jogador_venceu +=1

            else:
                print("\033[31mOpção inválida. Digite entre 1 e 3\33[m")

        elif computador == 2: # Computador escolheu TESOURA
            if jogador == 0: # Jogador escolheu PEDRA
                print("JOGADOR GANHOU")
                jogador_venceu +=1

            elif jogador == 1: # Jogador escolheu PAPEL
                print("COMPUTADOR GANHOU")
                computador_venceu += 1

            elif jogador == 2: # Jogador escolheu TESOURA
                print("EMPATE")
                empate += 1
        
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 3\33[m")
    
        print(f"Total de Empates: {empate}")
        print(f"Total de vitórias do Jogador: {jogador_venceu}")
        print(f"Total de vitórias do Computador: {computador_venceu}")
        print("\033[1;94m-\033[0;0m" *50)

menu()
