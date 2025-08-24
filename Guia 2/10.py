import random

def generarLista(lista):
    for _ in range(10):
        n = random.randint(1,100)
        lista.append(n)
    return lista

def filtrarImpares(lista):
    listaImpares = []
    impares = filter(lambda x: x % 2 != 0, lista)
    #return list(impares)
    for n in impares:
        listaImpares.append(n)
    return listaImpares

def main():
    listaRandom = []
    listaFiltrada = []
    listaRandom = generarLista(listaRandom)
    print(f"Lista generada\n{listaRandom}")
    listaFiltrada = filtrarImpares(listaRandom)
    print(f"Lista filtrada\n{listaFiltrada}")

main()