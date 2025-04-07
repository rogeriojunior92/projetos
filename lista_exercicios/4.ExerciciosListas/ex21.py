"""
21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, 
VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses 
carros faz com um litro de combustível. Calcule e mostre:

a) O modelo do carro mais econômico;
b) Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 
quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de
exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem
mudar a cada execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""

lista_carros = []
lista_km = []
lista_litros = []
lista_preco = []

gasolina = 2.25
for c in range(0, 5):
    print(f"Veículo {c+1}")
    carro = input("Nome: ")
    km = float(input("Quantos Km por litro? "))
    distancia = int(input("Digite a distância da viagem: "))
    print()

    lista_carros.append(carro)
    lista_km.append(km)

    litros = distancia / km
    preco = litros * 2.25

    lista_litros.append(litros)
    lista_preco.append(preco)

print("Relatório Final")
print(
f"\n{'1'} - {lista_carros[0]:^10} - {lista_km[0]:^10} - {lista_litros[0]:^10.2f}litros  -  R$ {lista_preco[0]:^5.2f}",
f"\n{'2'} - {lista_carros[1]:^10} - {lista_km[1]:^10} - {lista_litros[1]:^10.2f}litros  -  R$ {lista_preco[1]:^5.2f}",
f"\n{'3'} - {lista_carros[2]:^10} - {lista_km[2]:^10} - {lista_litros[2]:^10.2f}litros  -  R$ {lista_preco[2]:^5.2f}",
f"\n{'4'} - {lista_carros[3]:^10} - {lista_km[3]:^10} - {lista_litros[3]:^10.2f}litros  -  R$ {lista_preco[3]:^5.2f}",
f"\n{'5'} - {lista_carros[4]:^10} - {lista_km[4]:^10} - {lista_litros[4]:^10.2f}litros  -  R$ {lista_preco[4]:^5.2f}"
    )
print(f"O menor consumo é do veículo {min(lista_preco)}")