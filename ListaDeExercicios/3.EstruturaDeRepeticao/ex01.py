"""
01. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido. 
"""
nota = int(input("Favor, digite uma nota entre 0 e 10: "))
while nota <= 0 or nota >=10:
    nota = int(input("ERRO! Digite uma nota entre 0 e 10: "))
else:
    print("Valor inválido")