"""
Variáveis
"""

HORA_DIA = 8 # Representa o número de horas em um dia (padrão: 8 horas).
HORA_SEMANAL = 40 # Representa o número de horas em uma semana (padrão: 40 horas).
TOTAL_ANO_MESES = 12 # Representa o total de meses em um ano (padrão: 12 meses).

# -----------------------------------------------------------------------------------------------------------
def titulo(txt):

    """
    Função imprime um título com traços. Ela será usada para exibir títulos ao longo do código.
    """

    print('-' *70)
    print(txt)
    print('-' *70)

# -----------------------------------------------------------------------------------------------------------
def calcular_salario_hora(salario, horas_trabalhadas):

    """
    Calcula o salário por dia, semana, mês e ano com base no salário por hora e nas horas trabalhadas por semana.

    Args:
        salario (float): O valor do salário por hora.
        horas_trabalhadas (int): O número de horas trabalhadas por semana.

    Returns:
        tuple: Uma tupla contendo os salários calculados por dia, semana, mês e ano.
    """

    salario_dia = salario * HORA_DIA
    salario_semanal = salario * HORA_SEMANAL
    salario_mensal = salario * horas_trabalhadas
    salario_anual = salario * horas_trabalhadas * TOTAL_ANO_MESES

    return salario_dia, salario_semanal, salario_mensal, salario_anual

# -----------------------------------------------------------------------------------------------------------
def continuar():

    """
    Função pergunta ao usuário se ele deseja continuar. Se o usuário inserir "S" para sim, o cálculo continua. Se ele inserir "N" para não, o código termina.
    """

    while True:
        resp = input('Deseja continuar? [S/N] ').upper()[0]
        if resp in "SN":
            return resp
        print('Erro! Digite "S" para sim e "N" para não.')

# -----------------------------------------------------------------------------------------------------------
def main():

    """
    Função principal para execução do programa.
    """

    while True:

        titulo('Conversor Anual / Mensal / Semanal / Por Hora'.center(70))
        while True:
            try:
                salario = float(input('Digite o salario por hora R$ '))
                horas_trabalhadas = int(input('Digite a quantidade de horas trabalhado: '))
                break
            except ValueError:
                print('Por favor, insira um valor numérico válido.')

        # Calcular o salário por hora, dia, semana, mês e ano          
        salario_dia, salario_semanal, salario_mensal, salario_anual = calcular_salario_hora(salario, horas_trabalhadas)
    
        # Imprimir os resultados formatados
        print('-' *70)
        print(f'Salário por hora R$ {salario:>5.2f}')
        print(f'Salario por dia  R$ {salario_dia:>5.2f}')
        print(f'Salario semanal  R$ {salario_semanal:>5.2f}')
        print(f'Salario mensal   R$ {salario_mensal:>5.2f}')
        print(f'Salario anual    R$ {salario_anual:>5.2f}')
        print(f'Total de horas de trabalhado: {horas_trabalhadas} horas')
        print('-' *70)

        resp = continuar()
        if resp == "N":
            break

# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()