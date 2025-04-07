###################################################
# Tabuada Python com estrutura de repetição While #
###################################################

# O programa inicia em 1 e termina em 10
# O programa também pergunta se deseja continuar com a tabuada [S/N]

def titulo(txt):
    print("\033[96m-\033[0;0m" *30)
    print('\033[96m'+txt+'\033[0;0m')
    print("\033[96m-\033[0;0m" *30)

titulo("TABUADA PYTHON".center(30))
while True:
    valor = int(input("Quer ver qual tabuada? "))
    for c in range(1, 11):
        print(f"{valor} x {c} = {valor*c}")
    
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        print("\033[96m-\033[0;0m" *30)
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N")
    if resp == "N":
        break
print("\033[96m-\033[0;0m" *30)
