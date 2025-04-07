"""
48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

    Exemplo:

      12376489
      => 98467321
"""

lista_numero = []

for c in range(1, 10):
  num = int(input("Entre com o número: "))
  lista_numero.append(num)

lista_numero.reverse()
print(f"=> {lista_numero}")