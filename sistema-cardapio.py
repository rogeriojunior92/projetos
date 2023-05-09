cardapio = [[100, 'Hamburguer', 19.90], [101, 'Hot dog', 15.90], [102, 'X-Salada', 12.90], [103, 'X-Bacon', 14.90],
            [104, 'Coca-Cola', 5.90], [105, 'Guaraná', 4.90], [106, 'Água', 1.90]]

pedido = {}
lista_pedido = []
total_pedido = []

while True:
    print('-' *35)
    print(f"{'COD':<5}{'PRODUTO':<20} {'VALOR'}")
    print('-' *35)
    for lista in cardapio:
        print(f"{lista[0]:<5}{lista[1]:<20} R$ {lista[2]:.2f}")
    print('-' *35)
    
    pedido['codigo'] = int(input("Informe o código: "))
    if pedido['codigo'] == 0:
        print("\033[32mSaindo do programa. Até breve!\33[m")
        break

    while pedido['codigo'] < 100 or pedido['codigo'] > 106:
        print("\033[31mCódigo Inválido. Digite o código do cardapio.\33[m")
        pedido['codigo'] = int(input("Informe o código: "))

    for lista in cardapio:
        if pedido['codigo'] == lista[0]:
            pedido['quantidade'] = int(input("Informe a quantidade: "))
            pedido['lanche'] = lista[1]
            pedido['valor_pedido'] = lista[2] * pedido['quantidade']
   
    total_pedido.append(pedido['valor_pedido'])
    lista_pedido.append(pedido.copy())

print('-' *35)
print("SEU PEDIDO".center(35))
print('-' *35)
for lista in lista_pedido:
    print(f"{lista['quantidade']}x {lista['lanche']:<15}{lista['valor_pedido']:>15.2f}")
print('-' *35)
print(f"Total {sum(total_pedido):>27.2f}")