"""12. Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron."""

def verificarSocio(x):
    return len(x) == 5 and x.isdigit()

def registroSocios(listaI):
    while True:
        x = input("Ingrese su numero de socio: ")
        if x == "0":
            break
        if verificarSocio(x):
            listaI.append(x)
        else:
            print("Error, el numero de socio debe tener 5 digitos.")
    return listaI

def informeSocio(lista):
    listaR = []
    for socio in lista:
        cont = 0
        for i in range(len(lista)):
            if lista[i] == socio:
                cont += 1
        flag = False
        for r in listaR:
            if r == socio:
                flag = True
        if flag == False:
            listaR.append(socio)
            print(f"El socio {socio} ingreso {cont} veces en el dia.")


def eliminarIngreso(lista):
    cont = 0
    #listaO = lista.copy()
    listaO = lista[:]
    x = input("Ingrese el numero de socio para eliminar sus entradas del registro: ")
    while verificarSocio(x) == False:
        print("Error, el numero de socio debe tener 5 digitos.")
        x = input("Ingrese el numero de socio para eliminar sus entradas del registro: ")
    while x in lista:
        lista.remove(x)
        cont += 1
    return listaO, lista, cont

def main(): 
    listaR = []
    listaR = registroSocios(listaR)
    informeSocio(listaR)
    listaO, listaD, contE = eliminarIngreso(listaR)
    print(f"Registros antes de eliminar: {listaO}\nRegistros despues de eliminar: {listaD}\nCantidad de registros eliminados: {contE}")

main()