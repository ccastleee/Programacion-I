def añoBisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def fechaSiguiente(dia,mes,año):
    diaSiguente = dia+1
    fechaNueva = f"{diaSiguente},{mes},{año}"
    if mes == 2:
        if añoBisiesto(año):
            if diaSiguente > 29:
                fechaNueva = f"{1},{mes+1},{año}"
        else:
            if diaSiguente > 28:
                fechaNueva = f"{1},{mes+1},{año}"
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if diaSiguente > 30:
            fechaNueva = f"{1},{mes+1},{año}"
    else:
        if diaSiguente > 31:
            fechaNueva = f"{1},{mes+1},{año}"
    return fechaNueva

def sumarDias(dia,mes,año,N):
    for _ in range(N):
        dia, mes, año = map(int, fechaSiguiente(dia,mes,año).split(","))
    return f"{dia},{mes},{año}"

def cantidadDias(dia1,mes1,año1,dia2,mes2,año2):
    cont = 0
    while (dia1, mes1, año1) != (dia2, mes2, año2):
        dia1, mes1, año1 = map(int, fechaSiguiente(dia1, mes1, año1).split(","))
        cont += 1
    return cont

print(fechaSiguiente(27,2,2023))
print(sumarDias(25,2,2023, 5))
print(cantidadDias(25,2,2023, 2,3,2023))