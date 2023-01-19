"""
05. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. 
"""

def somaImposto(taxaImposto, custo):
    return (1 + taxaImposto/100) * custo

taxa = float(input("Digite a Taxa de Imposto: "))
c = float(input("Digite o custo: R$ "))
print(f"Valor do Imposto R$ {somaImposto(taxa,c):.2f}")