# Importar bibliotecas
import os
from time import sleep

# Lista com sublista com infs código, lanche e preço
cardapio = [[100, 'Hamburguer', 19.90], [101, 'Hot dog', 15.90], [102, 'X-Salada', 12.90], [103, 'X-Bacon', 14.90],
            [104, 'Coca-Cola', 5.90], [105, 'Guaraná', 4.90], [106, 'Água', 1.90]]

pedido = {} # Dicionário para armazenar chave e valor
lista_pedido = [] # Lista para armazenar os dados do dicionário
total_pedido = [] # Lista para calcular o valor total do pedido

os.system("cls")
while True:
    print('-' *35)
    print(f"{'COD':<5}{'PRODUTO':<20} {'VALOR'}")
    print('-' *35)
    # Iteração com a lista / sublista para visualização do carpadio 
    for lista in cardapio:
        print(f"{lista[0]:<5}{lista[1]:<20} R$ {lista[2]:.2f}")
    print('-' *35)
    print("Digite \033[32m0\33[m para encerrar o pedido")
    print('-' *35)

    # Input para entrada dos dados
    pedido['codigo'] = int(input("Informe o código: "))
    if pedido['codigo'] == 0:
        sleep(0.5)
        print("\033[32mSaindo do programa. Até breve!\33[m")
        break
    
    # Validação do pedido entre 100 e 106
    while pedido['codigo'] < 100 or pedido['codigo'] > 106:
        sleep(0.5)
        print("\033[31mCódigo Inválido. Digite o código do cardapio.\33[m")
        pedido['codigo'] = int(input("Informe o código: "))

    # Iteração com a lista / sublista 
    # Se o pedido for igual ao código da lista, irá trazer o pedido correto
    for lista in cardapio:
        if pedido['codigo'] == lista[0]:
            # Validação do pedido entre 100 e 106
            pedido['quantidade'] = int(input("Informe a quantidade: "))
            while pedido['quantidade'] < 1 or pedido['quantidade'] > 10:
                sleep(0.5)
                print("\033[31mERRO! Digite uma quantidade válida entre 0 e 10.\33[m")
                pedido['quantidade'] = int(input("Informe a quantidade: "))
            # Chave criada para buscar todos os lanches
            pedido['lanche'] = lista[1]
            # Chave criada para armazenar o preço * quantidade
            pedido['valor_pedido'] = lista[2] * pedido['quantidade']
   
    total_pedido.append(pedido['valor_pedido']) # Armazena a chave de preço * quantidade
    lista_pedido.append(pedido.copy()) # Lista para armazenar os dados do dicionário

sleep(0.5)
os.system("cls")
print('-' *35)
print("SEU PEDIDO".center(35))
print('-' *35)
# Iteração que percorre a lista e retorna a quantidade, lanches e valor do pedido
for lista in lista_pedido:
    print(f"{lista['quantidade']}x {lista['lanche']:<15}{lista['valor_pedido']:>15.2f}")
print('-' *35)
print(f"Total {sum(total_pedido):>27.2f}")
print('-' *35)