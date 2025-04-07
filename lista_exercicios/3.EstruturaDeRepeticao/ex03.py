"""
03. Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
"""

while True:
    nome = input("Digite o nome: ")
    if len(nome) < 3:
        nome = input("ERRO! Digite o nome: ")
        print(f"\033[32mSeja bem-vindo, {nome}\33[m")
        break

while True:
    idade = int(input("Idade: "))
    if idade < 1 or idade > 150:
        idade = int(input("ERRO! Digite entre 0 e 150: "))
        print(f"\033[32mVocê tem {idade} anos\33[m")
        break

while True:
    salario = float(input("Salário: R$ "))
    if salario < 1:
        salario = float(input("ERRO! Digie um salário maior que 0,00: R$ "))
        print(f"\033[32mSalário R$ {idade}\33[m")
        break

while True:
    sexo = input("Sexo: [M/F] ").upper()[0]
    if sexo in "MF":
        break
    print("\033[31mERRO! Digite apenas M ou F\33[m")


estado_civil = input("Digite o Estado Cívil [s, c, v ou d]: ").lower()[0]
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("\033[31mDados Inválidos.\33[m")
    estado_civil = input("Digite o Estado Cívil [s, c, v ou d]: ").lower()[0]
print(f"Você digitou {estado_civil}")