from random import randint as azar

def cargarLista(lista):
    for _ in range(azar(10,11)):
        n = int(azar(1000,9999))
        lista.append(n)
    return lista

def devolverProductoLista(lista):
    total = 1
    for n in lista:
        total *= n
    return total

def eliminarValor(lista):
    n = int(input("Ingrese el valor a eliminar: "))
    while n in lista:
        lista.remove(n)
    return lista

def esCapicua(lista):
    for i in range(len(lista)):
        if lista[i] != lista[-(i+1)]:
            return False
    return True

listaRandom = []
listaEjemplo = [50,17,91,17,50]
listaRandom = cargarLista(listaRandom)
print(f"Lista random: {listaRandom}")
print(f"El producto de la lista es: {devolverProductoLista(listaRandom)}")
print(f"Lista con el valor eliminado: {eliminarValor(listaRandom)}")
print(esCapicua(listaEjemplo))