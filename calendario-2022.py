import calendar

# Função para criar linha e texto
def titulo(txt):
    print("\033[1;94m-\033[0;0m" *75)
    print("\033[1;44m"+txt+"\033[1;0m")
    print("\033[1;94m-\033[0;0m" *75)


titulo("CALENDÁRIO 2022".center(75))
print(calendar.calendar(2022))
print("\033[1;94m-\033[0;0m" *75)
