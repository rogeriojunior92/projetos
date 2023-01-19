"""
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um 
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    a) Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    b) Triângulo Equilátero: três lados iguais;
    c) Triângulo Isósceles: quaisquer dois lados iguais;
    d) Triângulo Escaleno: três lados diferentes; 
"""
lado1 = int(input("Digite o primeiro lado do triângulo: "))
lado2 = int(input("Digite o segundo lado do triângulo: "))
lado3 = int(input("Digite o terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("Triângulo Equilátero: três lados iguais")
elif lado1 == lado2 != lado3:
    print("Triângulo Isósceles: quaisquer dois lados iguais")
elif lado1 != lado2 != lado3:
    print("Triângulo Escaleno: três lados diferentes")
