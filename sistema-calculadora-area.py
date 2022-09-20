import os
import math
from datetime import datetime
from time import sleep


def titulo(txt):
    print("\033[1;94m-\033[0;0m" *50)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *50)


def area_retangulo(altura, base):
    """
    A área do retângulo corresponde ao produto (multiplicação) da medida da base pela altura da figura, 
    sendo expressa pela fórmula: A = b x h
    A: área
    b: base
    h: altura
    """
    os.system("cls")
    titulo("ÁREA DO RETÂNGULO".center(50))
    area = altura * base
    sleep(0.5)
    print(f"Área de um terreno {altura} x {base} = {area:.2f}m²")
    os.system("pause")


def area_quadrado(lado):
    """
    A área do quadrado corresponde ao tamanho da superfície dessa figura, sendo expressa pela fórmula: 
    A = L2
    ou
    A = b.h
    """
    os.system("cls")
    titulo("ÁREA DO QUADRADO".center(50))
    area = lado ** 2
    sleep(0.5)
    print(f"Área do quadrado é {area:.2f}m²")
    os.system("pause")


def area_triangulo(altura, base):
    """
    A área do triângulo pode ser calculada através das medidas da base e da altura da figura. 
    Área: área do triângulo
    b: base
    h:altura
    """
    os.system("cls")
    titulo("ÁREA DO TRIÂNGULO".center(50))
    area = (base * altura) / 2
    sleep(0.5)
    print(f"Área de um triângulo é {area}m²")
    os.system("pause")


def area_circulo(raio):
    """
    A área do círculo corresponde ao valor da superfície dessa figura, levando em conta a medida de seu raio (r).
    Para calcular a área do círculo devemos utilizar a seguinte fórmula:
    A = π . r2
    """
    os.system("cls")
    titulo("ÁREA DO CIRCULO".center(50))
    area = math.pi * (raio * raio)
    sleep(0.5)
    print(f"A área do circulo é {area:.2f}m²")
    os.system("pause")


def area_trapezio(base_maior, base_menor, altura):
    """
    A área do trapézio mede o valor da superfície dessa figura plana formada por quatro lados.
    Sendo: A = B + b.h / 2
    A: área da figura
    B: base maior
    b: base menor
    h: altura
    """
    os.system("cls")
    titulo("ÁREA DO TRAPEZIO".center(50))
    area = (base_maior + base_menor) * (altura / 2)
    sleep(0.5)
    print(f"A área do trapézio é {area:.2f}m²")
    os.system("pause")


def area_losango(diag_maior, diag_menor):
    """
    Para calcular a área do losango é necessário traçar duas diagonais. 
    Dessa forma tem-se 4 triângulos retângulos (com ângulo reto de 90º) iguais.
    Sendo:
    A: a área do losango
    D1: a diagonal maior
    D2: a diagonal menor
    """
    os.system("cls")
    titulo("ÁREA DO LOSANGO".center(50))
    area = (diag_menor * diag_maior) / 2
    sleep(0.5)
    print(f"A área do Losango é {area}m²")
    os.system("pause")


def area_cone(raio, geratriz):
    """
    Para calcular a área do cone que pode ser dividido, para obter a superfície, em parte lateral e base.
    AL = π * raio * geratriz
    AT = π * raio * (geratriz + raio)
    """
    os.system("cls")
    titulo("ÁREA DO CONE".center(50))
    al = math.pi * raio * geratriz
    at = math.pi * raio * (geratriz + raio)
    sleep(0.5)
    print(f"Superfície lateral do cone {al:.2f}m²")
    sleep(0.5)
    print(f"Superficie do Cone {at:.2f}m²")
    os.system("pause")


def area_hexagono(perimetro, apotema):
    """
    Para o cálculo da superfície do hexágono, você precisa digitar a apótema (equivalente a metade da altura da figura)
    e o lado ou perímetro. Neste caso, a fórmula é igual a perímetro vezes apotema dividido por dois.
    """
    os.system("cls")
    titulo("ÁREA DO HEXÁGONO".center(50))
    metade = apotema / perimetro
    area = metade * 2
    sleep(0.5)
    print(f"Superficie do Hexágono {area:.2f}m²")
    os.system("pause")


def area_pentagono():
    os.system("cls")
    titulo("ÁREA DO PENTAGONO".center(50))

    os.system("pause")


def area_tetraedro(a):
    """
    Para o cálculo da área de tetraedro,  é um triângulo poligonal, com 3 faces triangulares iguais. 
    Portando, se você observar, esta figura geométrica é idêntica a uma pirâmide, ou seja, a base e todos os lados são congruentes o que o tonar regular. 
    Fórmula Total:  AT = a² * (**3)
    """
    os.system("cls")
    titulo("ÁREA DO TETRAEDRO".center(50))
    area = (a * a) * (a ** (1/3))


def menu():
    os.system("cls")
    while True:
        titulo("SISTEMA CALCULADORA DE ÁREA".center(50))
        print("1 - Área do Retângulo\n2 - Área do Quadrado\n3 - Área do Triângulo\n4 - Área do Círculo\n5 - Área do Trapézio\n6 - Área do Losango\n7 - Área do Cone\n8 - Área do Hexagono\n9 - Area do Pentagono\n10 - Área do Tetraedro\n11 - Sair")
        print("\033[1;94m-\033[0;0m" *50)

        opcao = int(input("Digite a sua opção: "))
        if opcao == 1:
            area_retangulo(float(input("ALTURA (m): ")), float(input("BASE (m): ")))
        elif opcao == 2:
            area_quadrado(float(input("Digite a alturado do quadrado: ")))
        elif opcao == 3:
            area_triangulo(float(input("Digite a altura do triângulo: ")), float(input("Digite a base do triângulo: ")))
        elif opcao == 4:
            area_circulo(float(input("Digite o valor do raio, para obter a área: ")))
        elif opcao == 5:
            area_trapezio(float(input("Digite o valor da base maior: ")), float(input("Digite o valor da base menor: ")), float(input("Digite a altura: ")))
        elif opcao == 6:
            area_losango(float(input("Digite o valor diagnonal menor: ")), float(input("Digite o valor diagnonal maior: ")))
        elif opcao == 7:
            area_cone(float(input("Digite o valor do raio: ")), float(input("Digite o valor geratriz: ")))
        elif opcao ==8:
            area_hexagono(float(input("Digite o valor do perimetro: ")), float(input("Digite o valor da apotema: ")))
        elif opcao == 9:
            area_pentagono()
        elif opcao == 10:
            area_tetraedro()
        elif opcao == 11:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 5\33[m")

menu()
