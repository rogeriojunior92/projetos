"""
15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada 
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

a) Mostre a quantidade de valores que foram lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem;
"""
lista_numero = []
soma = media = acima_media = abaixo_sete = 0

while True:
    num = int(input("Digite o valor: "))
    if num < 0:
        break
    soma += num
    lista_numero.append(num)

print("-" *50)
print(f"Quantidade de valores que foram lidos: {len(lista_numero)}")
print("-" *50)
print(f"Ordem valores na ordem em que foram informados: {lista_numero}")
lista_numero.reverse()
print("-" *50)
for lista in lista_numero:
    print(f"Ordem inversa valores na ordem em que foram informados: {lista}")
print("-" *50)
print(f"Soma dos valores: {soma}")
media = sum(lista_numero) / len(lista_numero)
print("-" *50)
print(f"Média dos valores: {media}")
print("-" *50)
for c in lista_numero:
    if c > media:
        acima_media += 1
    elif c < 7:
        abaixo_sete += 1
print("-" *50)
print(f"Quantidade de valores acima da média calculada: {acima_media}")
print("-" *50)
print(f"Quantidade de valores abaixo de sete: {abaixo_sete}")
print("-" *50)