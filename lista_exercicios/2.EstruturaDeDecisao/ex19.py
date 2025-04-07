"""
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 
"""

testar = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for num in testar:
    centena = num // 100 % 10
    dezena = num // 10 % 10
    unidade = num // 1 % 10
    milhar = num // 1000

    print(f"{num} = {milhar} milhares, {centena} centenas, {dezena} dezenas e {unidade} unidades")