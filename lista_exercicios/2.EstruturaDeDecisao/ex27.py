"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
"""
morango = int(input("Quantidade de morangos (em Kg): "))
maca = int(input("Quantidade de maças (em Kg): "))

morango_ate_5kg = morango * 2.50
morango_acima_5kg = morango * 2.20

maca_ate_5kg = maca * 1.80
maca_acima_5kg = maca * 1.5


if morango > 5:
    preco_morango = morango_ate_5kg
else:
    preco_morango = morango_acima_5kg

if maca > 5:
    preco_maca = maca_ate_5kg
else:
    preco_maca = maca_acima_5kg

qtde = morango + maca
total = preco_morango + preco_maca

if qtde > 8 or total > 25:
    desc = total * 10/100
else:
    desc = 'Não possui desconto'
    print(f"{desc}")

print("-" *40)
print(f"Quantidade de Morango: {morango}")
print(f"Quantidade de Maças: {maca}")
print(f"Quantidade total de frutas: {qtde}Kg")
print(f"Valor total R$ {total:.2f}")
print("-" *40)
print(f"Desconto de 10% sobre este total R$ {desc:.2f}")
print("-" *40)