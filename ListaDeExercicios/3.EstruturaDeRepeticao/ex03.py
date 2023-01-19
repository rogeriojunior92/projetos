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
        print("ERRO! Digite o nome novamente.")
        break