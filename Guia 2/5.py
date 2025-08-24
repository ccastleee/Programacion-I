def verificarLista(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                return False
    return True

lista = [1,2,3,4]
print(verificarLista(lista))