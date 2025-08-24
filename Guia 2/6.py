def normalizarLista(lista):
    listaN = []
    sumList = sum(lista)
    for num in lista:
        elemNorm = num/sumList
        listaN.append(elemNorm)
    return listaN

listaO = [1,1,3]
listaN = normalizarLista(listaO)
print(listaN)