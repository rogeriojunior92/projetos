"""
02. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações. 
"""
usuario = input("Login: ")
senha = input("Senha: ")

while usuario == senha:
    print("ERRO! Digite o usuário e senha corretamente")
    usuario = input("Login: ")
    senha = input("Senha: ")
else:
    print("Acesso concedido")