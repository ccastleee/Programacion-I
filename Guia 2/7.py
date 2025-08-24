def intercalarLista(lista1,lista2):
    rango = min(len(lista1),len(lista2))
    for i in range(rango):
        lista1[i*2+1:i*2+1] = [lista2[i]]
    lista1[len(lista1):] = lista2[rango:]
    return lista1

lista1 = [8,1,3]
lista2 = [5,9,7,11,12]
print(intercalarLista(lista1,lista2))
