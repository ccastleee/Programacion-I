def añoBisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def diaDeLaSemana(dia,mes,año):
    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2
    siglo = año // 100
    año2 = año % 100
    diaSem = (((26*mes-2)//10)+dia+año2+(año//4)+(siglo//4)-(2*siglo))%7
    if diaSem < 0:
        diaSem += 7
    return diaSem

def diasDeMes(mes, año):
    dias = 0
    if mes == 2:
        if añoBisiesto(año):
            dias = 29
        else:
            dias = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias = 30
    else:
        dias = 31
    return dias

def imprimirCalendario(mes, año):
    print(" D  L  M  X  J  V  S")
    primerDia = diaDeLaSemana(1, mes, año)
    diasMes = diasDeMes(mes, año)
    for _ in range(primerDia):
        print("   ", end="")
    dia = 1
    while dia <= diasMes:
        if dia < 10:
            print(" ", end="")
            print(dia, end=" ")
        else:
            print(dia, end=" ")
        if (primerDia + dia) % 7 == 0:
            print()
        dia += 1

imprimirCalendario(8,25)