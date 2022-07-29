import os
from datetime import datetime
from time import sleep

'''
LOJA GAMER VIRTUAL
Em andamento...
'''


catalogo_completo = ("PS3", 2500.00, "PS4", 3900.00, "PS5", 4990.00, "Nintendo Switch", 2100.00, "XBOX Series", 4500.00,
                    "Headset sem fio", 520.00, "Controle PS5 DualSense", 390.00, "Controle Switch - Pro Controller", 340.00, "Controle PS4 - Dual Shok 4", 289.90, "Controle PS4 - Dual Shok 3", 220.90,
                    "Mini Console Retro - 20 Mil Jogos", 389.90, "Controle USB para PC", 49.90, "Controle Arcade USB", 349.90,
                    "Elden Ring - PS5 (Mídia Física)", 289.90, "Metroid Dread - Nintendo Switch", 319.90, "Battlefield - Xbox Series (Mídia Física)", 59.90, "FIFA 2022 - PS5 (Mídia Física)", 119.90, "Back 4 Blood Br - Ps4 (Mídia Física)", 69.90, "GTA 5 - PS5 (Mídia Física)", 199.90, "F1 2022 BR - PS5 (Mídia física)", 299.90, "Pokemon Legends Arceus - Switch", 319.90,
                    "HD SSD Kingston 480GB - SATA 2.5", 389.90, "HD SSD Kingston 240GB - SATA 2.5", 219.90, "HD Externo 2TB Seagate - USB 3.0", 429.90, "Memoria DDR4 8Gb 2666 Kingston", 229.90, "HD Externo 1TB Seagate - USB 3.0", 329.90)

catalogo = {
    "video_game": {
        "100": ["PS3", 2500.00],
        "101": ["PS4", 3900.00],
        "102": ["PS5", 4990.00],
        "103": ["Nintendo Switch", 2100.00],
        "104": ["XBOX Series", 4500.00],
    },

    "acessorios": {
        "110": ["Headset sem fio", 520.00],
        "111": ["Controle PS5 DualSense", 390.00],
        "112": ["Controle Switch - Pro Controller", 340.00],
        "113": ["Controle PS4 - Dual Shok 4", 289.90],
        "114": ["Controle PS3 - Dual Shok 3", 220.90],
    },

    "selecao_retro": {
        "120": ["Mini Console Retro - 20 Mil Jogos", 389.90],
        "121": ["Controle USB para PC", 49.90],
        "122": ["Controle Arcade USB", 349.90],
    },

    "selecao_jogos": {
        "130": ["Elden Ring - PS5 (Mídia Física)", 289.90],
        "131": ["Metroid Dread - Nintendo Switch", 319.90],
        "132": ["Battlefield - Xbox Series (Mídia Física)", 59.90],
        "133": ["FIFA 2022 - PS5 (Mídia Física)", 119.90],
        "134": ["Back 4 Blood Br - Ps4 (Mídia Física)", 69.90],
        "135": ["GTA 5 - PS5 (Mídia Física)", 199.90],
        "136": ["F1 2022 BR - PS5 (Mídia física)", 299.90],
        "137": ["Pokemon Legends Arceus - Switch", 319.90],
    },

    "selecao_hardware": {
        "140": ["HD SSD Kingston 480GB - SATA - 2.5", 389.90],
        "141": ["HD SSD Kingston 240GB - SATA - 2.5", 219.90],
        "142": ["HD Externo 2TB Seagate - USB 3.0", 429.90],
        "143": ["Memoria DDR4 8Gb 2666 Kingston", 229.90],
        "144": ["HD Externo 1TB Seagate - USB 3.0", 329.90],
    }
}

lista_pedido = []


# Função para criar linha e texto
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


def resposta():
    while True:
        resp = input("Deseja escolher algo mais? [S/N] ").upper()[0]
        if resp in "SN":
            break
    if resp == "N":
        print("Saindo da tela...")


def catalogo_preco():
    os.system("cls")
    titulo("CATÁLOGO COMPLETO".center(50))
    for c in range(0, len(catalogo_completo), 2):
        print(f"{catalogo_completo[c]:.<40} R$ {catalogo_completo[c+1]:>6.2f}")
    print("\033[1;94m-\033[0;0m" *50)


def catalogo_video_game():
    total_video_game = 0
    os.system("cls")
    catalogo_preco()
    titulo("CATÁLOGO DE VIDEO GAMES".center(50))
    print("1 - PS3\n2 - PS4\n3 - PS5\n4 - Nintendo Switch\n5 - Xbox Series\n6 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para comprar Video-Game: ")
    if opcao == 1:
        total_video_game += catalogo["video_game"]["100"][1]
        lista_pedido.append(total_video_game)
        print(f'Você escolheu PS3 R$ {catalogo["video_game"]["100"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 2:
        total_video_game += catalogo["video_game"]["101"][1]
        lista_pedido.append(total_video_game)
        print(f'Você escolheu PS4 R$ {catalogo["video_game"]["101"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 3:
        total_video_game += catalogo["video_game"]["102"][1]
        lista_pedido.append(total_video_game)
        print(f'Você escolheu PS5 R$ {catalogo["video_game"]["102"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 4:
        total_video_game += catalogo["video_game"]["103"][1]
        lista_pedido.append(total_video_game)
        print(f'Você escolheu Nintendo Switch R$ {catalogo["video_game"]["103"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 5:
        total_video_game += catalogo["video_game"]["104"][1]
        lista_pedido.append(total_video_game)
        print(f'Você escolheu Xbox Series R$ {catalogo["video_game"]["104"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 6:
        print("\033[32mSaindo do catálogo de video game\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")
    print("\033[1;94m-\033[0;0m" *50)


def catalogo_acessorios():
    total_acessorios = 0
    os.system("cls")
    catalogo_preco()
    titulo("CATÁLOGO DE ACESSÓRIOS".center(50))
    print("1 - Headset sem fio\n2 - Controle PS5 DualSense\n3 - Controle Switch - Pro Controller\n4 - Controle PS4 - Dual Shok 4\n5 - Controle PS3 - Dual Shok 3\n6 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para comprar Video-Game: ")
    if opcao == 1:
        total_acessorios += catalogo["acessorios"]["110"][1]
        lista_pedido.append(total_acessorios)
        print(f'Você escolheu Headset sem fio R$ {catalogo["acessorios"]["110"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 2:
        total_acessorios += catalogo["acessorios"]["111"][1]
        lista_pedido.append(total_acessorios)
        print(f'Você escolheu Controle PS5 DualSense R$ {catalogo["acessorios"]["111"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 3:
        total_acessorios += catalogo["acessorios"]["112"][1]
        lista_pedido.append(total_acessorios)
        print(f'Você escolheu Controle Switch - Pro Controller R$ {catalogo["acessorios"]["112"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 4:
        total_acessorios += catalogo["acessorios"]["113"][1]
        lista_pedido.append(total_acessorios)
        print(f'Você escolheu Controle PS4 - Dual Shok 4 R$ {catalogo["acessorios"]["113"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 5:
        total_acessorios += catalogo["acessorios"]["114"][1]
        lista_pedido.append(total_acessorios)
        print(f'Você escolheu Controle PS3 - Dual Shok 3 R$ {catalogo["acessorios"]["114"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 6:
        print("\033[32mSaindo do catálogo de acessórios\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")   
    print("\033[1;94m-\033[0;0m" *50)


def catalogo_secao_retro():
    total_retro = 0
    os.system("cls")
    catalogo_preco()
    titulo("CATÁLOGO DE SEÇÃO RETRÔ".center(50))
    print("1 - Mini Console Retro - 20 Mil Jogos\n2 - Controle USB para PC\n3 - Controle Arcade USB\n4 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para comprar Video-Game: ")
    if opcao == 1:
        total_retro += catalogo["selecao_retro"]["120"][1]
        lista_pedido.append(total_retro)
        print(f'Você escolheu Mini Console Retro - 20 Mil Jogos R$ {catalogo["selecao_retro"]["120"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 2:
        total_retro += catalogo["selecao_retro"]["121"][1]
        lista_pedido.append(total_retro)
        print(f'Você escolheu Controle USB para PC R$ {catalogo["selecao_retro"]["121"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 3:
        total_retro += catalogo["selecao_retro"]["122"][1]
        lista_pedido.append(total_retro)
        print(f'Você escolheu Controle Arcade USB R$ {catalogo["selecao_retro"]["122"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 4:
        print("\033[32mSaindo do catálogo de seção retrô\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 4\33[m")  
    print("\033[1;94m-\033[0;0m" *50)


def catalogo_jogos():
    total_jogos = 0
    os.system("cls")
    catalogo_preco()
    titulo("CATÁLOGO DE JOGOS".center(50))
    print("1 - Elden Ring - PS5 (Mídia Física)\n2 - Metroid Dread - Nintendo Switch\n3 - Battlefield - Xbox Series (Mídia Física)\n4 - FIFA 2022 - PS5 (Mídia Física)\n5 - Back 4 Blood Br - Ps4 (Mídia Física)\n6 - GTA 5 - PS5 (Mídia Física)\n7 - F1 2022 BR - PS5 (Mídia física)\n8 - Pokemon Legends Arceus - Switch\n9 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para comprar Video-Game: ")
    if opcao == 1:
        total_jogos += catalogo["selecao_jogos"]["130"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu Elden Ring - PS5 (Mídia Física) R$ {catalogo["selecao_jogos"]["130"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 2:
        total_jogos += catalogo["selecao_jogos"]["131"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu Metroid Dread - Nintendo Switch R$ {catalogo["selecao_jogos"]["131"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 3:
        total_jogos += catalogo["selecao_jogos"]["132"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu Battlefield - Xbox Series (Mídia Física) R$ {catalogo["selecao_jogos"]["132"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 4:
        total_jogos += catalogo["selecao_jogos"]["133"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu FIFA 2022 - PS5 (Mídia Física) R$ {catalogo["selecao_jogos"]["133"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 5:
        total_jogos += catalogo["selecao_jogos"]["134"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu Back 4 Blood Br - Ps4 (Mídia Física) R$ {catalogo["selecao_jogos"]["134"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 6:
        total_jogos += catalogo["selecao_jogos"]["135"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu GTA 5 - PS5 (Mídia Física) R$ {catalogo["selecao_jogos"]["135"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 7:
        total_jogos += catalogo["selecao_jogos"]["136"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu F1 2022 BR - PS5 (Mídia física) R$ {catalogo["selecao_jogos"]["136"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 8:
        total_jogos += catalogo["selecao_jogos"]["137"][1]
        lista_pedido.append(total_jogos)
        print(f'Você escolheu Pokemon Legends Arceus - Switch R$ {catalogo["selecao_jogos"]["137"][1]:.2f}. Deseja adicionar algo mais? ')
    elif opcao == 9:
        print("\033[32mSaindo do catálogo de jogos\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 9\33[m")  
    print("\033[1;94m-\033[0;0m" *50)


def catalogo_hardware():
    total_hardware = 0
    os.system("cls")
    catalogo_preco()
    titulo("CATÁLOGO DE HARDWARE".center(50))
    print("1 - HD SSD Kingston 480GB - SATA - 2.5\n2 - HD SSD Kingston 240GB - SATA - 2.5\n3 - HD Externo 2TB Seagate - USB 3.0\n4 - Memoria DDR4 8Gb 2666 Kingston\n5 - HD Externo 1TB Seagate - USB 3.0\n6 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção para comprar Video-Game: ")
    if opcao == 1:
        total_hardware += catalogo["selecao_hardware"]["140"][1]
        lista_pedido.append(total_hardware)
        print(f'Você escolheu HD SSD Kingston 480GB - SATA - 2.5 R$ {catalogo["selecao_hardware"]["140"][1]}. Deseja adicionar algo mais? ')
    elif opcao == 2:
        total_hardware += catalogo["selecao_hardware"]["141"][1]
        lista_pedido.append(total_hardware)
        print(f'Você escolheu  HD SSD Kingston 240GB - SATA - 2.5 R$ {catalogo["selecao_hardware"]["141"][1]}. Deseja adicionar algo mais? ')
    elif opcao == 3:
        total_hardware += catalogo["selecao_hardware"]["142"][1]
        lista_pedido.append(total_hardware)
        print(f'Você escolheu HD Externo 2TB Seagate - USB 3.0 R$ {catalogo["selecao_hardware"]["142"][1]}. Deseja adicionar algo mais? ')
    elif opcao == 4:
        total_hardware += catalogo["selecao_hardware"]["143"][1]
        lista_pedido.append(total_hardware)
        print(f'Você escolheu Memoria DDR4 8Gb 2666 Kingston R$ {catalogo["selecao_hardware"]["143"][1]}. Deseja adicionar algo mais? ')
    elif opcao == 5:
        total_hardware += catalogo["selecao_hardware"]["144"][1]
        lista_pedido.append(total_hardware)
        print(f'Você escolheu HD Externo 1TB Seagate - USB 3.0 R$ {catalogo["selecao_hardware"]["144"][1]}. Deseja adicionar algo mais? ')
    elif opcao == 6:
        print("\033[32mSaindo do catálogo de hardware\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 6\33[m")  
    print("\033[1;94m-\033[0;0m" *50)


def fechar_pedido():
    os.system("cls")
    titulo("FECHAR PEDIDO DE COMPRA".center(50))
    data = datetime.now()
    data_registro = data.strftime("%d/%m/%Y %H:%M")
    print(f"Horário do Pedido: {data_registro}")
    for pedido in lista_pedido:
        print(f"R$ {pedido:.2f}")
    valor_total = sum(lista_pedido)
    sleep(0.5)
    print("\033[1;94m-\033[0;0m" *50)
    print(f"R$ {valor_total:.2f}")
    print("\033[1;94m-\033[0;0m" *50)
    os.system("pause")


def menu():
    titulo("SISTEMA DE LOJA GAMER PYTHON".center(50))
    print("1 - Visualizar Catálogo de Preços\n2 - Visualizar Catálogo de Vídeo Game\n3 - Visualizar Catálogo de Acessórios\n4 - Visualizar Catálogo de Seção Retrô\n5 - Visualizar Catálogo de Jogos\n6 - Visualizar Catálogo de Hardware\n7 - Fazer Pedido\n8 - Fechar Pedido\n9 - Sair")
    print("\033[1;94m-\033[0;0m" *50)

    opcao = leiaInt("Digite a sua opção: ")
    if opcao == 1:
        catalogo_preco()
    elif opcao == 2:
        catalogo_video_game()
    elif opcao == 3:
        catalogo_acessorios()
    elif opcao == 4:
        catalogo_secao_retro()
    elif opcao == 5:
        catalogo_jogos()
    elif opcao == 6:
        catalogo_hardware()
    elif opcao == 7:
        catalogo_video_game()
        resposta()
        catalogo_acessorios()
        resposta()
        catalogo_secao_retro()
        resposta()
        catalogo_jogos()
        resposta()
        catalogo_hardware()
        menu()
    elif opcao == 8:
        fechar_pedido()
    elif opcao == 9:
        print("\033[32mSaindo do programa... Agradecemos pela preferência. Volte Sempre!\33[m")
    else:
        print("\033[31mOpção inválida. Digite entre 1 e 9\33[m")

menu()
