"""1. Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha 
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al 
segundo se considerará que el primero corresponde al día anterior. En ningún 
caso la diferencia en horas puede superar las 24 horas."""

fechas = ("26/09/25", "27/09/25", "28/09/25", "29/09/25")

horarios = [(21,30),(22,30),(23,30),(23,45)]

def verificarInput(x):
    return len(x) == 2 and x.isdigit()

def validarOpcion(x):
    return x >= 1 and x <= len(fechas)

def verificarFechaHorario():
    dia = input("Ingrese el dia (solo 2 digitos): ")
    while not verificarInput(dia):
        print("Error, ingreso invalido.")
        dia = input("Ingrese el dia (solo 2 digitos): ")
    mes = input("Ingrese el mes (solo 2 digitos): ")
    while not verificarInput(mes):
        print("Error, ingreso invalido.")
        mes = input("Ingrese el mes (solo 2 digitos): ")
    año = input("Ingrese el año (solo 2 digitos): ")
    while not verificarInput(año):
        print("Error, ingreso no valido.")
        año = input("Ingrese el año (solo 2 digitos): ")
    
    fecha = f"{dia}/{mes}/{año}"

    if fecha not in fechas:
        print("Fecha no valida!")
    else:
        print("Fecha valida.")

def sumarDias():
    i=0
    print("Que fecha desear actualizar?")
    for fecha in fechas:
        print(f"{i+1} - {fecha}")
        i+=1
    opcion = int(input("Seleccione la opcion: "))
    while not validarOpcion(opcion):
        i = 0
        print("Error, opcion incorrecta.")
        for fecha in fechas:
            print(f"{i+1} - {fecha}")
            i+=1
        opcion = int(input("Seleccione la opcion: "))
    suma = int(input("Cuantos dias desea sumar a la fecha?: "))
    fechasLista = list(fechas)
    fechaSplit = fechasLista[opcion-1].split('/')
    fechaNueva = int(fechaSplit[0])+suma
    fechaSplit[0] = str(fechaNueva)
    fechasLista[opcion-1] = ('/').join(fechaSplit)
    fechasNuevo = tuple(fechasLista)
    print(fechasNuevo)

def verificarHorario():
    horario = input("Ingrese el horario: ")
    while not verificarInput(horario):
        print("Error, ingreso no valido.")
        horario = input("Ingrese el horario: ")
    if int(horario) not in horarios:
        print("Horario no valido.")
    else:
        print("Horario valido.")

def diferenciaHorarios(h1, h2):
    dif = h2 - h1
    if not 0>=h1<=24 or 0>=h2<=24:
        raise ValueError("Error, fuera de rango.")
    elif h1 > h2:
        


verificarFechaHorario()
sumarDias()
verificarHorario()