from tkinter import *

root = Tk()
root.title("Calculadora de IMC")
root.geometry("260x230")
root.configure(background="#dde")

CheckVar1 = IntVar()
CheckVar2 = IntVar()


def calculo_imc():
    alt = float(f"{altura.get()}")
    kg = float(f"{peso.get()}")
    imc = kg / alt **2

    resultado = imc

    if imc < 18.5:
        print(f"Altura: {alt:.2f}")
        print(f"Peso: {kg:.2f}kg") 
        resultado_texto['text'] = "IMC é: Abaixo do Peso"
    
    elif imc >= 18.5 and imc <= 25:
        print(f"Altura: {alt:.2f}")
        print(f"Peso: {kg:.2f}kg")
        resultado_texto['text'] = "IMC é : Normal"
    
    elif imc >= 25 and imc <= 30:
        print(f"Altura: {alt:.2f}")
        print(f"Peso: {kg:.2f}kg")
        resultado_texto['text'] = "IMC é: Sobrepeso"
   
    else:
        print(f"Altura: {alt:.2f}")
        print(f"Peso: {kg:.2f}kg")
        resultado_texto['text'] = "IMC é: Obesidade"
    
    label_resultado['text'] = f"{resultado:.2f}"


Label(root, text="Altura", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
altura = Entry(root)
altura.place(x=10, y=30, width=100, height=20)

Label(root, text="Peso", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)
peso = Entry(root)
peso.place(x=10, y=80, width=100, height=20)

Label(root, text="Sexo", background="#dde", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)
c1 = Checkbutton(root, text='Masculino', background="#dde", foreground="#009", anchor=W, variable=CheckVar1, onvalue=0, offvalue=1)
c1.place(x=10, y=130, width=100, height=20)

c2 = Checkbutton(root, text='Feminino', background="#dde", foreground="#009", anchor=W, variable=CheckVar1, onvalue=1, offvalue=0)
c2.place(x=10, y=150, width=100, height=20)

label_resultado = Label(root, text='---', background="#dde", foreground="#009", width=37, height=1, padx=6, pady=12, relief='flat', anchor='center', font='Ivy 24 bold')
label_resultado.place(x=140, y=10, width=100, height=100)

resultado_texto = Label(root, text='', background="#dde", foreground="#009", width=37, height=1, padx=0, pady=0, relief='flat', anchor=W)
resultado_texto.place(x=150, y=90)

Button(root, text="Calcular", command=calculo_imc).place(x=10, y=180, width=100, height=30)
Button(root, text="Sair", command=quit).place(x=120, y=180, width=100, height=30)

root.mainloop()