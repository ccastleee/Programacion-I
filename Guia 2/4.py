def listaResultante(lista1, lista2):
    for num in lista2:
        lista1.remove(num)
    listaR = lista1
    return listaR

def main():
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [2,5,10,1,7]
    print(f"Lista original\n{lista1}")
    print(f"Lista de valores a eliminar\n{lista2}")
    listaR = listaResultante(lista1, lista2)
    print(f"Lista original modificada\n{lista1}")
    print(f"Lista resultante\n{listaR}")

main()