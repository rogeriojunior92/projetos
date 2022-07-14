from tkinter import *


def novo_arquivo():
    try:
        arquivo = open("agenda.txt", "wt+")
        arquivo.close()
    except:
        print("\033[31mOcorreu um erro na criação do arquivo\33[m")
    else:
        print("\033[32mArquivo criado com sucesso\33[m")


def imprimir_dados():
    arquivo = open("agenda.txt", "a", encoding="utf-8")
    arquivo.write("\nNome.....: %s" % nome.get())
    arquivo.write("\nTelefone.: %s" % telefone.get())
    arquivo.write("\nE-mail...: %s" % email.get())
    arquivo.write("\nOBS......: %s" % obs.get("1.0", END))
    arquivo.write("\n")
    arquivo.close()


root = Tk()
root.title("Tela de Cadastro")
root.geometry("400x300")
root.configure(background="#dde")

Label(root, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
nome = Entry(root)
nome.place(x=10, y=30, width=200, height=20)

Label(root, text="Telefone", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)
telefone = Entry(root)
telefone.place(x=10, y=80, width=200, height=20)

Label(root, text="E-mail", background="#dde", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)
email = Entry(root)
email.place(x=10, y=130, width=200, height=20)

Label(root, text="Observação", background="#dde", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)
obs = Text(root)
obs.place(x=10, y=180, width=300, height=80)

Button(root, text="Gravar", command=imprimir_dados).place(x=10, y=270, width=100, height=20)
Button(root, text="Sair", command=quit).place(x=120, y=270, width=100, height=20)


root.mainloop()
