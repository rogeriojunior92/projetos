"""
04. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.
"""

texto = input("Digite algo: ")
if len(texto) > 10:
    texto = input("ERRO! Digite até 10 caracteres> ")
