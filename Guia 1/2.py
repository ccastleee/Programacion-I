def esBisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def validarFecha(dia, mes, año):
    validarF = False
    if dia <= 0 or mes <= 0 or año <= 0:
        validarF = False
    elif mes == 2:
        if esBisiesto(año):
            if 1<=dia<=29:
                validarF = True
        else:
            if 1<=dia<=28:
                validarF = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1<=dia<=30:
            validarF = True
    else:
        if 1<=dia<=31:
            validarF = True
    return validarF

print(validarFecha(29,2,2024))