"""
19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado 
da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não 
deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções
devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a
percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa,
e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

lista_windows_server = []
lista_unix = []
lista_linux = []
lista_netware = []
lista_mac_os = []
lista_outro = []

ws = unix = linux = netware = macos = outro = 0


def titulo(txt):
    print("\033[34m-\33[m" *40)
    print("\033[34m"+txt+"\33[m")
    print("\033[34m-\33[m" *40)


def menu():
    ws = unix = linux = netware = macos = outro = 0
    while True:
        titulo("SISTEMA OPERACIONAL".center(40))
        print("1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\n7 - Resultado Votação\n0 - Sair")
        print("\033[34m-\33[m" *40)

        opcao = int(input("Digite a sua opção: "))
        if opcao == 1:
            lista_windows_server.append(ws)
            ws += 1
            print("Você votou no Sistema Operacional - Windows Server")
        elif opcao == 2:
            lista_unix.append(unix)
            unix += 1
            print("Você votou no Sistema Operacional - Unix")
        elif opcao == 3:
            lista_linux.append(linux)
            linux += 1
            print("Você votou no Sistema Operacional - Linux")
        elif opcao == 4:
            lista_netware.append(netware)
            netware += 1
            print("Você votou no Sistema Operacional - Netware")
        elif opcao == 5:
            lista_mac_os.append(macos)
            macos +=1
            print("Você votou no Sistema Operacional - Mac OS")
        elif opcao == 6:
            lista_outro.append(outro)
            outro += 1
            print("Você votou no Sistema Operacional - Outro")
        elif opcao == 7:
            titulo("RESULTADO DA VOTAÇÃO".center(40))
            print(f"{'Sistema Operacional':^20}         {'Votos':^5}   {'%':^3}")
            print("-------------------         -----   ----")
            print(f"{'Windows Server'}              {ws:^5}  {len(lista_windows_server) / ws *100:^3}%")
            print(f"{'Unix'}                        {unix:^5}  {len(lista_unix) *100:^3}%")
            print(f"{'Linux'}                       {linux:^5}  {len(lista_linux) *100:^3}%")
            print(f"{'Netware'}                     {netware:^5}  {len(lista_netware) *100:^3}%")
            print(f"{'Mac OS '}                     {macos:^5}  {len(lista_mac_os) *100:^3}%")
            print(f"{'Outro'}                       {outro:^5}  {len(lista_outro) *100:^3}%")
            print("-------------------         ----- ")
            print("Total                        {}")
 
        elif opcao == 0:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção Inválida. Digite apenas 0 até 6")

menu()
