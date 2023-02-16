"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
"""

morango_ate_5kg = 2.50
maca_ate_5kg = 1.80

morango_acima_5kg = 2.20
maca_acima_5kg = 1.50

qtde_morango = int(input("Digite a quantidade de morangos (kg): "))
qtde_maca = int(input("Digite a quantidade de maça (kg): "))

if qtde_morango <= 5:
    valor_morango = qtde_morango * morango_ate_5kg
else:
    valor_morango = qtde_morango * morango_acima_5kg

if qtde_maca > 5:
    valor_maca = qtde_maca * maca_acima_5kg
else:
    valor_maca = qtde_maca * maca_ate_5kg

print("-" *40)
valor_total = valor_morango + valor_maca
print(f"Valor Total R$ {valor_total:.2f}")
if valor_total > 25 or (qtde_morango + qtde_maca) > 8:
    desc = valor_total * 0.1
    print(f"Desconto de 10% R$ {desc}")