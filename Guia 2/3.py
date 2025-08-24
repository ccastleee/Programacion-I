def validarN():
    n = int(input("Ingrese: "))
    while n < 0:
        print("Error, ingrese un valor positivo.")
        n = int(input("Ingrese: "))
    return n
        

def agregarN(lista):
    print("Ingrese un numero para el rango de la lista")
    n = validarN()
    for i in range(1, n+1):
        lista.append(i**2)
    return lista

listaC = []
listaC = agregarN(listaC)
print(listaC)
print(f"Ultimos 10 valores de la lista:\n{listaC[-10:]}")