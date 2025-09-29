lista = [1,2,3,4,5]

lista.pop()
lista.append("hola")

print(lista)

lista_1 = [2,5,10,1,3,4]

def ordenarLista(lista):
    for i in range(len(lista)):
        minIndice = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minIndice]:
                minIndice = j
        auxIndice = lista[i]
        lista[i] = lista[minIndice]
        lista[minIndice] = auxIndice
    return lista

ordenarLista(lista_1)
print(lista_1)