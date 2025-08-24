from random import randint as azar

def validarDatos():
    n = int(input("Ingrese la cantidad de elemetos que va a ingresar en la lista: "))
    while n < 0:
        print("Error, no puede ingresar un valor negativo.")
        n = int(input("Ingrese la cantidad de elemetos que va a ingresar en la lista: "))
    return n

def cargarLista(lista):
    cantElem = validarDatos()
    for _ in range(cantElem):
        n = azar(1,100)
        lista.append(n)
    return lista

def verificarLista(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def devolverLista(lista):
    listaU = []
    #for num in lista:
        #if num not in listaU:
            #listaU.append(num)
    for num1 in lista:
        agregar = True
        for num2 in listaU:
            if num1 == num2:
                agregar = False
        if agregar:
            listaU.append(num1)
    return listaU

listaR = []
listaR = cargarLista(listaR)
print(listaR)
print(verificarLista(listaR))
listaU = devolverLista(listaR)
print(listaU)