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
    return fechasNuevo[opcion-1]

def verificarHorario():
    horario = input("Ingrese el horario: ")
    while not verificarInput(horario):
        print("Error, ingreso no valido.")
        horario = input("Ingrese el horario: ")
    if int(horario) not in horarios:
        print("Horario no valido.")
    else:
        print("Horario valido.")

def elegirHorarioDeLista():
    print("Elija un horario:")
    for i, (hh, mm) in enumerate(horarios, start=1):
        print(f"{i} - {hh:02d}:{mm:02d}")
    while True:
        try:
            op = int(input("Opción: "))
            if 1 <= op <= len(horarios):
                return horarios[op-1]
            print("Opción fuera de rango.")
        except ValueError:
            print("Ingrese un número entero.")

def diferenciaHorarios(h1, h2):

    h1Total = h1[0]*60 + h1[1]
    h2Total = h2[0]*60 + h2[1]

    if h1Total > h2Total:
        h2Total += 24*60

    diff = h2Total - h1Total
    return (diff // 60, diff % 60)

def main():
    global fechas

    print("\n(a) Ingresar una fecha y verificar:")
    verificarFechaHorario()  

    print("\n(b) Sumar N días a una fecha:")
    fechas = sumarDias()  
    print(f"Fecha actualizada: {fechas}")

    print("\n(c) Ingresar/Elegir horarios válidos y (d) calcular diferencia:")
    print("Horario 1:")
    h1 = elegirHorarioDeLista()   
    print("Horario 2:")
    h2 = elegirHorarioDeLista()

    dh, dm = diferenciaHorarios(h1, h2)

    print(f"Diferencia: {str(dh).zfill(2)}:{str(dm).zfill(2)}")

main()