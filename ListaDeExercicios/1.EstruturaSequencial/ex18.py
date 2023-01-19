"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download 
do arquivo usando este link (em minutos). 

Fórmula:

   a) Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) = tempo em segundos.
   b) Um arquivo de 15 MB, baixado a 10 Mb/s: 15 / (10/8) = 12 segundos.

"""

tamanho = float(input("Digite o tamanho dp arquivo para download (em MB): "))
link_internet = float(input("Digite a velocidade de um link de Internet (em Mbps): "))
download = (tamanho / link_internet) * 60

print()
print(f"Tamanho do arquivo de {tamanho}MB\nLink de internet de {link_internet}Mb/s\nTempo {download:.0f} segundos para concluir download.")
