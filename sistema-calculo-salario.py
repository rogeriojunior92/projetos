# Importar bibliotecas
import os

# ---------------------------------------------------------------------------------------------------------
# Função para criar título
def titulo(txt):

    print('\033[34m-\33[m' *85)
    print('\033[34m'+txt+'\033[m')
    print('\033[34m-\33[m' *85)

# ---------------------------------------------------------------------------------------------------------
# Função para calcular o salário
def calculo_salario(hora_trabalhada, horas_trabalhada_mes):

    salario = hora_trabalhada * horas_trabalhada_mes
    return salario

# ---------------------------------------------------------------------------------------------------------
# Função para calcular o desconto do salário
def desconto_salario(salario):

    descontoIR = 0
    impostoIR = 0
    inss = salario * 0.10
    fgts = salario * 0.11
    sindicato = salario * 0.03
    
    if salario < 900:
        descontoIR = 'Isento'
        totalDesconto = sindicato + inss
        salarioLiquido = salario - totalDesconto

    elif salario > 900 and salario <= 1500:
        impostoIR = 5
        descontoIR = salario * 0.05
        totalDesconto = sindicato + inss + descontoIR
        salarioLiquido = salario - totalDesconto
    
    elif salario > 1500 and salario <= 2500:
        impostoIR = 10
        descontoIR = salario * 0.1
        totalDesconto = sindicato + inss + descontoIR
        salarioLiquido = salario - totalDesconto
    
    elif salario > 2500:
        impostoIR = 20
        descontoIR = salario * 0.2
        totalDesconto = sindicato + inss + descontoIR
        salarioLiquido = salario - totalDesconto

    return descontoIR, impostoIR, inss, fgts, sindicato, totalDesconto, salarioLiquido

# ---------------------------------------------------------------------------------------------------------
# Função que executa todo o processo
def main():

    while True:

        hora_trabalhada = float(input('Digite o valor/hora cobrado: '))
        while hora_trabalhada < 1 or hora_trabalhada > 100:
            print('\033[31mDados Inválidos. Digite o valor/hora correto.\033[m')
            hora_trabalhada = float(input('Digite o valor/hora cobrado: '))

        horas_trabalhada_mes = int(input('Digite a quantidade de horas trabalhadas no mês: '))
        while horas_trabalhada_mes < 1 or horas_trabalhada_mes > 200:
            print('\033[31mDados Inválidos. Digite a quantidade de horas trabalhadas no mês.\033[m')
            horas_trabalhada_mes = int(input('Digite a quantidade de horas trabalhadas no mês: '))
                
        salario = calculo_salario(hora_trabalhada, horas_trabalhada_mes)
        descontoIR, impostoIR, inss, fgts, sindicato, totalDesconto, salarioLiquido = desconto_salario(salario)

        os.system('cls')
        print('  ')
        titulo('EXTRATO BASE DE SALÁRIO'.center(85))
        print(f'Salário Bruto                   : R$ {salario:.2f}')
        print('\033[34m-\33[m' *85)
        print(f'(-) IR ({impostoIR}%)                    : R$ {descontoIR:.2f}')
        print(f'(-) INSS ( 10%)                 : R$ {inss:.2f}')
        print(f'(-) SINDICATO ( 3%)             : R$ {sindicato:.2f}')
        print(f'FGTS (11%)                      : R$ {fgts:.2f}')
        print(f'Total de descontos              : R$ {totalDesconto:.2f}')
        print('\033[34m-\33[m' *85)
        print(f'Salário Liquido                 : R$ {salarioLiquido:.2f}')
        print('\033[34m-\33[m' *85)
        print('  ')

        while True:
            resp = input("Deseja continuar? [S/N] ").upper()[0]
            if resp in 'SN':
                break
            print('\033[31mDados Inválidos. Digite S ou N.\033[m')
        if resp == 'N':
            print('Saindo do Programa. Até breve!')
            break
            
# ---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()