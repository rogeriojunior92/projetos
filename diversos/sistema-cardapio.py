# Importar bibliotecas
import os
from time import sleep

# -----------------------------------------------------------------------------------------------------------
def titulo(txt):

    print('\033[34m-\033[m' *45)
    print('\033[34m'+txt+'\033[m')
    print('\033[34m-\033[m' *45)

# -----------------------------------------------------------------------------------------------------------
def exibir_cardapio(cardapio):

    """
    Exibe o cardápio na tela.
    """

    print('\033[34m-\033[m' *45)
    print(f"{'COD':<5}{'PRODUTO':<20}{'VALOR':>20}")
    print('\033[34m-\033[m' *45)
    # Iteração com a lista / sublista para visualização do carpadio 
    for lista in cardapio:
        print(f"{lista[0]:<5}{lista[1]:<20}{lista[2]:>20.2f}")
    print('\033[34m-\033[m' *45)

# -----------------------------------------------------------------------------------------------------------
def fazer_pedido(cardapio):
    
    """
    Permite ao usuário fazer um pedido, escolhendo itens do cardápio e suas quantidades.
    - O usuário pode escolher itens do cardápio e suas quantidades.
    - O pedido é armazenado em uma lista chamada lista_pedido.
    - O usuário pode digitar 0 para encerrar o pedido ou -1 para visualizar o pedido atual a qualquer momento.
    """

    lista_pedido = list()
    while True:
        pedido = dict()
        pedido['codigo'] = int(input("Informe o código: "))
        if pedido['codigo'] == 0:
            sleep(0.5)
            print("\033[32mSaindo do programa. Até breve!\33[m")
            break
        elif pedido['codigo'] == -1:
            sleep(0.5)
            exibir_cardapio(lista_pedido)
            continue
        
        item_encontrado = False
        for item in cardapio:
            if pedido['codigo'] == item[0]:
                item_encontrado = True
                break
        
        if not item_encontrado:
            sleep(0.5)
            print("\033[31mCódigo Inválido. Digite o código do cardápio.\33[m")
            continue
        
        pedido['quantidade'] = int(input('Informe a quantidade: '))
        # Validação do pedido entre 100 e 106
        while pedido['quantidade'] < 1 or pedido['quantidade'] > 10:
            sleep(0.5)
            print("\033[31mERRO! Digite uma quantidade válida entre 0 e 10.\33[m")
            pedido['quantidade'] = int(input("Informe a quantidade: "))
        
        pedido['lanche'] = item[1]
        pedido['valor_pedido'] = item[2] * pedido['quantidade']
        lista_pedido.append(pedido)

# -----------------------------------------------------------------------------------------------------------
def exibir_pedido(pedido):

    """
    Exibe o pedido atual do usuário na tela.
    """

    titulo("SEU PEDIDO".center(45))
    total_pedido = 0
    # Iteração que percorre a lista e retorna a quantidade, lanches e valor do pedido
    for item in pedido:
        print(f"{item['quantidade']}x {item['lanche']:<15}{item['valor_pedido']:>15.2f}")
        total_pedido += item['valor_pedido']
    print('-' *45)
    print(f"Total {total_pedido:>27.2f}")
    print('-' *45)

# -----------------------------------------------------------------------------------------------------------
def remover_pedido(pedido):

    """
    Permite ao usuário remover um item específico do pedido.
    """

    print("\nSelecione o item que deseja remover:")
    for i, item in enumerate(pedido):
        print(f"{i + 1}: {item['lanche']} (Quantidade: {item['quantidade']})")

        while True:
            try:
                opcao = int(input('Informe o número do item (0 para cancelar): '))
                if opcao == 0:
                    break
                elif 1 <= opcao <= len(pedido):
                    print("Item removido com sucesso!")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Tente novamente.")

# -----------------------------------------------------------------------------------------------------------
def adicionar_mais():

    while True:
        resposta = input('Deseja adicionar mais algum item ao pedido? [S/N] ').strip().upper()[0]
        if resposta == 'Sn':
            return True
        elif resposta == 'Nn':
            return False
        else:
            print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")

# -----------------------------------------------------------------------------------------------------------
def main():

    """
     Função principal que executa todo o programa.
    """

    # Lista com sublista com infs código, lanche e preço
    cardapio = [[100, 'Hamburguer', 19.90], [101, 'Hot dog', 15.90], [102, 'X-Salada', 12.90], [103, 'X-Bacon', 14.90],
                [104, 'Coca-Cola', 5.90], [105, 'Guaraná', 4.90], [106, 'Água', 1.90]]

    os.system("cls")
    exibir_cardapio(cardapio)

    global lista_pedido
    lista_pedido = list()
    fazer_pedido(cardapio)

    sleep(0.5)
    os.system("cls")
    exibir_pedido(lista_pedido)

    while adicionar_mais():

        novo_pedido = fazer_pedido(cardapio)
        lista_pedido.extend(novo_pedido)

        sleep(0.5)
        os.system("cls")
        exibir_pedido(lista_pedido)
    
    print("\nPedido finalizado. Obrigado!")

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()