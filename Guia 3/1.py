"""1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera sea el valor ingresado."""

def validarPositivo(x):
    return x > 0

def validarPositivos(x,y):
    return x > 0 and y > 0

#def imprimirMatriz(matriz):

def filasColumnas():
    numN = int(input("Ingrese el numero N x N de la matriz: "))
    while validarPositivo(numN) == False:
        print("Error, debe ser un numero positivo.")
        numN = int(input("Ingrese el numero N x N de la matriz: "))
    return numN

def valoresMatriz():
    n = int(input("Ingrese los valores: "))
    return n

def generarMatriz(numN):
    matriz = []
    for _ in range(numN):
        fila = []
        for _ in range(numN):
            fila.append(valoresMatriz())
        matriz.append(fila)
        print(matriz)
    return matriz

def ordenarMatriz(matriz):
    #for i in range(len(matriz)):
        #matriz[i] = sorted(matriz[i])
    #return matriz
    matrizOrdenada = [sorted(fila) for fila in matriz]
    return matrizOrdenada

def intercambiarFila(a, b, matriz):
    #aux = matriz[a-1]
    #matriz[a-1] = matriz[b-1]
    #matriz[b-1] = aux
    rangoFilas = len(matriz)
    matrizFila = matriz.copy() # en este caso no modifico la original, ya que hago un reemplazo de filas!
    while True:
        if validarPositivos(a,b) and a <= rangoFilas and b <= rangoFilas:
            break
        else:
            print(f"Numeros fuera de rango,el rango debe estar entre 1 y {rangoFilas}.")
    matrizFila[a-1], matrizFila[b-1] = matrizFila[b-1], matrizFila[a-1]
    return matrizFila

def intercambiarColumnas(col1, col2, matriz):
    matrizColumna = [fila[:] for fila in matriz] # en este caso tengo que hacer una copia profunda, ya que sino modifico la original!
    for i in range(len(matriz)):
        matrizColumna[i][col1-1], matrizColumna[i][col2-1] = matrizColumna[i][col2-1], matrizColumna[i][col1-1]
    return matrizColumna

def matrizT(matriz):
    matrizTraspuesta = [fila[:] for fila in matriz]
    for i in range(len(matrizTraspuesta)):
        for j in range(i+1, len(matrizTraspuesta)):
            matrizTraspuesta[i][j], matrizTraspuesta[j][i] = matrizTraspuesta[j][i], matrizTraspuesta[i][j]
    return matrizTraspuesta

def promedioFila(f, matriz):
    fila = matriz[f-1]
    suma = 0
    for n in fila:
        suma += n
    promedio = round(suma/len(fila), 1)
    return promedio

def porcentajeImparColumna(c, matriz):
    cont = 0
    for i in range(len(matriz)):
        if matriz[i][c-1] % 2 != 0:
            cont += 1
    porcentaje = (cont/len(matriz))*100
    return porcentaje

def esSimetricaPrincipal(matriz):
    return matrizT(matriz) == matriz

def esSimetricaSecundaria(matriz):
    lenght = len(matriz)
    for i in range(lenght):
        for j in range(lenght):
            if matriz[i][j] != matriz[lenght-1-j][lenght-1-i]: # i+j = n-1 (n orden de matriz)
                return False
    return True

def esPalindromo(matriz):
    listaPalindromo = []
    for col in range(len(matriz)):
        esPalindromo = True
        for fil in range(len(matriz)//2):
            if matriz[fil][col] != matriz[-(fil+1)][col]:
                esPalindromo = False
        if esPalindromo:
            listaPalindromo.append(col+1)
    return listaPalindromo


def main():
    numN = filasColumnas()
    matriz = generarMatriz(numN)
    print(f"Matriz {numN}x{numN}:\n{matriz}")
    print(f"Matriz ordenada\n{ordenarMatriz(matriz)}")
    print(f"Matriz con filas intercambiadas\n{intercambiarFila(2, 1, matriz)}")
    print(f"Matriz con columnas intercambiadas\n{intercambiarColumnas(1, 2, matriz)}")
    print(f"Matriz traspuesta\n{matrizT(matriz)}")
    print(f"Promedio de la fila: {promedioFila(2, matriz)}")
    print(f"Porcentaje de numeros impares de la columna: {porcentajeImparColumna(2, matriz)}%")
    if esSimetricaPrincipal(matriz):
        print("Es simetrica por diagonal principal!")
    else:
        print("No es simetrica por diagonal principal!")
    if esSimetricaSecundaria(matriz):
        print("Es simetrica por diagonal secundaria!")
    else:
        print("No es simetrica por diagonal secundaria!")
    if esPalindromo(matriz):
        print(f"Lista con columnas palindromas\n{esPalindromo(matriz)}")
    else:
        print("No hay columnas palindromas.")

main()