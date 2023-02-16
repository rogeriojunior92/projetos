"""
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
valor do desconto e valor a pagar. 
"""
total = 0

print("-" *30)
print("1 - File Duplo\n2 - Alcatra\n3 - Picanha\n0 - Sair")
print("-" *30)

tipo = int(input("Digite o tipo de carne: "))
qtde_carne = int(input("Digite a quantidade de carne: "))
cartao = input("Cartão Tabajara [S/N]? ").upper()[0]

if tipo == 1:
    carne = "File Duplo"
    if qtde_carne < 5:
        preco = qtde_carne * 4.90
    else:
        preco = qtde_carne * 5.80

elif tipo == 2:
    carne = "Alcatra"
    if qtde_carne < 5:
        preco = qtde_carne * 5.90
    else:
        preco = qtde_carne * 6.80

elif tipo == 3:
    carne = "Picanha"
    if qtde_carne < 5:
        preco = qtde_carne * 6.90
    else:
        preco = qtde_carne * 7.80

if cartao == "S":
    resp = "Sim"
    desc = preco * 5/100
elif cartao == "N":
    resp = "Não"
    total = preco

print()
print("--------------------- CUPOM FISCAL ---------------------")
print(f"Carne........................................ {carne}")
print(f"Quantidade................................... {qtde_carne}Kg")
print(f"Preço..................................... R$ {preco:.2f}")
print(f"Cartão Tabajara.............................. {resp}")
print(f"Total com desconto........................ R$ {desc:.2f}")
print(f"Valor Total............................... R$ {total:.2f}")
print("---------------------------------------------------------")