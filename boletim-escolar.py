import os
from time import sleep

ficha_aluno = []


'''
Função para criar titulo + linhas
'''
def titulo(txt):
    print("\033[34m-\033[0;0m" *40)
    print('\033[34m'+txt+'\033[0;0m')
    print("\033[34m-\033[0;0m" *40)


'''
Função que lê apenas número inteiro válido
'''
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(TypeError, ValueError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
            return 0
        else:
            return num

'''
Função para criar um arquivo novo
'''
def novo_arquivo():
    os.system("cls")
    try:
        arquivo = open("boletim_aluno.txt", "wt+")
        arquivo.close()
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na criação do arquivo.\33[m")
    else:
        sleep(0.5)
        print("\033[32mArquivo criado com sucesso\33[m")
    os.system("pause")


'''
Função para cadastrar um novo aluno
'''
def novo_cadastro():
    os.system("cls")
    print("\033[32mFavor, preencher os campos abaixo para cadastrar um aluno\33[m")
    sleep(0.5)
    matricula = int(input("Matrícula Escolar do aluno(a): "))
    nome = input("Nome do aluno(a): ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    ficha_aluno.append([matricula, nome, [nota1, nota2], media])

    '''
    Variável para escrita do arquivo e salvar no bloco de notas
    '''
    try:
        arquivo = open("boletim_aluno.txt", "at")
    except:
        sleep(0.5)
        print("\033[31mOcorreu um erro na abertura do arquivo.\33[m")
    else:
        try:
            arquivo.write(f"{ficha_aluno}")
        except:
            sleep(0.5)
            print("\033[31mOcorreu um erro na escrita do arquivo.\33[m")
        else:
            sleep(0.5)
            print("\033[32mCadastrado com sucesso\33[m")
    os.system("pause")


'''
Função para imprimir e/ou listar o cadastro
'''
def imprimir_cadastro():
    os.system("cls")
    sleep(0.5)
    print("ID".center(3), end='')
    print("Matricula".center(20), end='')
    print("Nome".center(20), end='')
    print("Notas".center(20), end='')
    print("Média".center(20))

    '''
    Loop para percorrer a lista e criar indice e/ou posição
    '''
    for indice_aluno in list(enumerate(ficha_aluno, start=1)):

        indice = indice_aluno[0]
        aluno = indice_aluno[1]

        print(str(indice).center(3), end='')
        print(str(aluno[0]).center(20), end='')
        print(str(aluno[1]).center(20), end='')
        print(str(aluno[2]).center(20), end='')
        print(str(aluno[3]).center(20))
    os.system("pause")


'''
Função para buscar aluno através da matrícula
'''
def buscar_cadastro():
    os.system("cls")
    termo = int(input("Informe a Matrícula Escolar do aluno(a) que deseja buscar: "))
    sleep(0.5)
    for identificador in ficha_aluno:
        matricula, nome, notas, media = identificador
        if matricula == termo:
            print("\033[32mColetando as informações...\33[m")
            sleep(0.5)
            print("\033[34m-\033[0;0m" *40)
            print(f"Matrícula: {matricula}\nNome: {nome}\nNotas: {notas}\nMédia: {media}")
            print("\033[34m-\033[0;0m" *40)
    os.system("pause")

'''
Função para deletar aluno através da matrícula
'''
def deletar_cadastro():
    os.system("cls")
    termo = int(input("Informe a Matrícula Escolar do aluno(a) que deseja excluir: "))
    sleep(0.5)
    for identificador in ficha_aluno:
        matricula, nome, notas, media = identificador
        if matricula == termo:
            ficha_aluno.remove([matricula, nome, notas, media])
            sleep(0.5)
            print(f"Matrícula \033[32m{termo}\33[m excluído com sucesso")
    os.system("pause")


'''
Função principal que executa todo o processo
'''
def menu():
    while True:
        titulo("BOLETIM ESCOLAR".center(40))
        print("1 - NOVO ARQUIVO\n2 - NOVO CADASTRO\n3 - IMPRIMIR CADASTRO\n4 - BUSCAR CADASTRO\n5 - DELETAR CADASTRO\n6 - SAIR")
        print("\033[34m-\033[0;0m" *40)
        print(f"Ao todo foram cadastrados {len(ficha_aluno)} aluno(as)")
        print("\033[34m-\033[0;0m" *40)

        opcao = leiaInt("Digite a sua opção: ")
        if opcao == 1:
            novo_arquivo()
        elif opcao == 2:
            novo_cadastro()
        elif opcao == 3:
            imprimir_cadastro()
        elif opcao == 4:
            buscar_cadastro()
        elif opcao == 5:
            deletar_cadastro()
        elif opcao == 6:
            print("\033[32mSaindo do programa... Até logo!\33[m")
            break
        else:
            print("\033[31mOpção inválida. Digite entre 1 e 6!\33[m")
        
menu()
