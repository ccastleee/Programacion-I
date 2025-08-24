"""Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como número de afiliado."""

def verificarAfiliado(lista0,lista1):
    while True:
        x = input("Ingrese el numero de afiliado (ingrese '-1' para salir): ")
        if x == "-1":
            break
        if len(x) != 4 or x == "":
            print("Numero de afiliado erroneo.")
        y = input("Si viene por urgencia ingrese '0', en caso de tener turno ingrese '1': ")
        if len(x) == 4 and y == "0":
            lista0.append(x)
            lista0.append("Urgencia")
        else:
            lista1.append(x)
            lista1.append("Turno")
    return lista0, lista1

def cantidadAfiliado(lista0,lista1):
    while True:
        contUrg = 0
        contTur = 0
        numAfi = input("Ingrese el numero del afiliado (ingrese '-1' para salir): ")
        if numAfi == "-1":
            break
        if len(numAfi) == 4:
                for i in range(0,len(lista0),2):
                    if lista0[i] == numAfi:
                        contUrg += 1
                for i in range(0, len(lista1),2):
                    if lista1[i] == numAfi:
                        contTur += 1
                if contUrg == 0 and contTur == 0:
                    print(f"El afiliado {numAfi} no se encuentra en los registros o no existe.")
                else:
                    print(f"El afiliado {numAfi} se atendio {contUrg} veces con Urgencia.")
                    print(f"El afiliado {numAfi} se atendio {contTur} veces con Turno.")
        else:
            print("Error, ingrese un numero de afiliado correcto.")

def main():
    listaUrgencia = []
    listaTurno = []
    listaUrgencia, listaTurno = verificarAfiliado(listaUrgencia, listaTurno)
    if len(listaUrgencia) == 0 and len(listaTurno) == 0:
        print("Sin registros.")
    else:
        print(listaUrgencia)
        print(listaTurno)
        cantidadAfiliado(listaUrgencia,listaTurno)

main()