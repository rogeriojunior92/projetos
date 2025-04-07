"""
37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte 
a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o 
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
"""
codigo_mais_alto = codigo_mais_baixo = 0
codigo_mais_gordo = codigo_mais_magro = 0
altura_mais_alto = altura_mais_baixo = 0 
peso_mais_gordo = peso_mais_magro = 0
media_altura = media_peso = 0

while True:
    codigo = int(input("Código: "))
    if codigo == 0:
        break
    print("Saindo do Programa.")

    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    if altura > altura_mais_alto:
        altura_mais_alto = altura
        codigo_cliente_mais_alto = codigo
    
    if altura < altura_mais_baixo:
        altura_mais_baixo = altura
        codigo_cliente_mais_baixo = codigo
    
    if peso > peso_mais_gordo:
        peso_mais_gordo = peso
        codigo_cliente_mais_gordo = codigo
    
    if peso < peso_mais_magro:
        peso_mais_magro = peso
        codigo_cliente_mais_magro = codigo

print("")