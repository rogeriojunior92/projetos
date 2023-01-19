"""
13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas 
ocorreram (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).

"""
temperatura_media = []

lista_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for c in range(12):
    media = float(input(f"Digite a temperatura de {lista_mes[c]}: "))
    temperatura_media.append(media)

media = sum(temperatura_media) / 12

for c in range(12):
    if temperatura_media[c] > media:
        print(f"{c} - {lista_mes[c]}: {media:.1f}º")