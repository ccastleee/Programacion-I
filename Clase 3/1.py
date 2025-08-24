m = [[1,2],[3,4],[5,6]]

print(m[0][1])

m[0] = [10,11]

print(m[0])
print(m)

filas = 3
columnas = 4
matriz = []

for f in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(0)

matriz = CrearMatriz()
filas = len(matriz)
columnas = len(matriz[0])
for f in range(filas):
    for c in range(columnas):
        n = int(input("Ingrese un numero: "))
        matriz[f][c] = n

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(filas):
            print("3%d", matriz[f][c], end="")
        print()