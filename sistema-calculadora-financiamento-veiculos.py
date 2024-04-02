import os

# -----------------------------------------------------------------------------------------------------------
def titulo(txt):
    
    """
    Nesta função, titulo, o valor txt é passado como parametro.
    A função tem o objetivo de imprimir um texto centralizado entre duas linhas de traços ("-")
    """

    print('-' *70)
    print(txt)
    print('-' *70)

# -----------------------------------------------------------------------------------------------------------
def calcular_financiamento(preco_inicial, valor_entrada, tempo_financiamento, taxa_juros):

    """
    Nesta função, calcular_financiamento, os valores de preco_inicial, valor_entrada, tempo_financiamento e taxa_juros são passados como parâmetros. 
    A função calcula o total financiado subtraindo o valor da entrada do preço inicial. Em seguida, calcula o pagamento mensal estimado dividindo o total financiado pelo tempo de
    financiamento em meses. O valor total pago no financiamento é calculado multiplicando o pagamento mensal pelo tempo de financiamento. Finalmente, o valor total de juros
    pagos é calculado multiplicando o total financiado pela taxa de juros e pelo tempo de financiamento.
    """

    # Calcula o total financiado
    total_financiamento = preco_inicial - valor_entrada
    # Calculando o pagamento mensal estimado usando a fórmula da amortização constante
    pagamento_mensal = total_financiamento / tempo_financiamento
    # Calculando o valor total de juros pagos
    total_juros = total_financiamento * taxa_juros * tempo_financiamento
    # Calculando o valor total pago no financiamento
    total_pago = total_financiamento + total_juros

    return total_financiamento, pagamento_mensal, total_pago, total_juros

# -----------------------------------------------------------------------------------------------------------
def continuar():

    """
    Na função continuar, o programa pergunta ao usuário se ele deseja continuar ou não. Se o usuário digitar 'S' ou 'N', a função retorna essa resposta. Caso contrário, 
    exibe uma mensagem de erro e continua pedindo uma entrada válida até que o usuário digite 'S' ou 'N'.
    """

    while True:
        resp = input("Deseja continuar? [S/N] ").upper()[0]
        if resp in "SN":
            return resp        
        print("\033[31mErro! Digite 'S' para sim e 'N' para não.\33[m")

# -----------------------------------------------------------------------------------------------------------
def main():

    """
    Função que executa todo o processo.
    """
    os.system("cls")
    while True:
        try:
            preco_inicial = float(input("Preço inicial do veículo: R$ "))
            valor_entrada = float(input("Valor da entrada: R$ "))
            taxa_juros = float(input("Taxa de juros (%): ")) / 100 # Convertendo a taxa de juros para a forma decimal
            tempo_financiamento = int(input("Tempo de financiamento (em meses): "))           

            total_financiamento, pagamento_mensal, total_pago, total_juros  = calcular_financiamento(preco_inicial, valor_entrada, tempo_financiamento, taxa_juros)

            titulo('CALCULADORA DE FINANCIAMENTO DE VEÍCULO'.center(70))
            print(f"O valor total financiado é: R$ {total_financiamento:.2f}")
            print(f"O pagamento mensal estimado é: R$ {pagamento_mensal:.2f}/mês")
            print(f"O valor total pago no financiamento é: R$ {total_pago:.2f}")
            print(f"O valor total de juros pagos é: R$ {total_juros:.2f}")
            print('-' *70)
        
        except ValueError:
            print('\033[31mErro: Entrada inválida. Certifique-se de inserir valores numéricos corretos.\033[m')
        except ZeroDivisionError:
            print('\033[31mErro: Tempo de financiamento não pode ser zero.\033[m')

        resp = continuar()
        if resp == "N":
            print("Saindo do Programa!")
            break

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()