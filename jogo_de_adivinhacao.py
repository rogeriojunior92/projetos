import random

# -----------------------------------------------------------------------------------------------------------
"""
Para contar o número de tentativas que o jogador fez.
"""
tentativas = 0

# -----------------------------------------------------------------------------------------------------------
def titulo(txt):

    """
    Função imprime um título centralizado com bordas de traços. Ela será usada para exibir títulos ao longo do jogo.
    """

    print('-' *50)
    print(f'{txt}'.center(50))
    print('-' *50)

# -----------------------------------------------------------------------------------------------------------
def pedir_numero_computador():

    """
    Função gera e retorna um número aleatório entre 1 e 10, que será o número que o jogador precisa adivinhar.
    """

    computador = random.randint(1, 10)
    return computador

# -----------------------------------------------------------------------------------------------------------
def pedir_numero_jogador():

    """
    Função solicita ao jogador que insira um número entre 1 e 10 e retorna o número inserido pelo jogador.
    """

    while True:
        try:
            jogador = int(input('Adivinhe o número que pensei (entre 1 e 10): '))
            while jogador < 1 or jogador > 10:
                print('\033[31mPor favor, digite um número válido entre 1 e 10.\033[m')
                jogador = int(input('Adivinhe o número que pensei (entre 1 e 10): '))
            else:
                return int(jogador)
        except ValueError:
            print('\033[31mPor favor, digite um número válido.\033[m')

# -----------------------------------------------------------------------------------------------------------
def iniciar_jogo(jogador, computador):

    """
    Função com dois parâmetros, "jogador e computador", que representam os números inseridos pelo jogador e o número gerado aleatoriamente pelo computador.
    Ela também conta o número de tentativas que o jogador fez.
    """

    global tentativas

    titulo('JOGADOR x COMPUTADOR'.center(50))
    print(f'Jogador: {jogador}')
    print(f'Computador: {computador}')
    print('-' *50)

    while True:
        if jogador == computador:
            print(f'Parabéns, você acertou o número após {tentativas} tentativas.')
            break
        elif jogador > computador:
            print(f'Jogador escolheu {jogador} x {computador} Comutador.')
            print('Tente um número menor.')
        else:
            print(f'Computador escolheu {computador} x {jogador} Jogador.')
            print('Tente um número maior.')
        print('-' *50)
        
        tentativas +=1
        jogador = pedir_numero_jogador() # Esta linha chama a função pedir_numero_jogador() para solicitar um novo número ao jogador. 
                                         # Este novo número substituirá o valor anterior de jogador na próxima iteração do loop.

# -----------------------------------------------------------------------------------------------------------
def continuar_jogo():

    """
    Função pergunta ao jogador se ele deseja continuar jogando. Se o jogador inserir "S" para sim, o jogo continua. Se ele inserir "N" para não, o jogo termina.
    """

    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
           return resp 
        print('\033[31mERRO! Favor, digitar apenas S ou N.\33[m')

# -----------------------------------------------------------------------------------------------------------
def main():
    
    """
    Função que executa todo o processo
    """

    while True:
        titulo('JOGO DE ADIVINHAÇÃO'.center(50))
        jogador = pedir_numero_jogador()
        computador = pedir_numero_computador()
        iniciar_jogo(jogador, computador)
        if not continuar_jogo():
            break

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()