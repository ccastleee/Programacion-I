listaImpar = [n for n in range(1,12) if n % 2 != 0]

print(listaImpar)
largo = len(listaImpar)
lista1 = listaImpar[:largo//2]
lista2 = listaImpar[largo//2:]

print(lista1)
print(lista2)

matriz = [[1,2,3],[1,2,3],[1,2,3]]

def matrizDiagonal(matriz, n = 0):
    fil = len(matriz)
    col = len(matriz[0])
    cont = 0
    if fil == col:
        for i in range(fil):
            if n == matriz[i][i]:
                cont += 1
    else:
        raise ValueError("Error, matriz no cuadrada.")
    if cont > 0:    
        print(f"El numero {n} aparece {cont} en la diagonal principal.")
    else:
        print("No se encuentra el numero en la diagonal principal.")

matrizDiagonal(matriz,2)

numeros = [1,2,3,4,5,6,7,8,9,10]

filtrados = list(filter(lambda x: x > 5 and x % 2 == 0, numeros))

print(filtrados)

lista = [0,1,2,3]
print(lista[::-1])

lst = [10,20,30,40,50,60]

lstR = lst[2:5]

print(lstR)

lst = [10,20,30,40,50]

resultado = [x for x in lst if x % 20 == 0]

print(resultado)

cuadrados = [n*n for n in [1,2,3]]
print(cuadrados)

nums = [1,2,3]

def sumarImpares(lista):
    suma = 0
    for num in lista:
        if num % 2 != 0:
            suma += num
    return suma

print(sumarImpares(nums))

mayores = len([x for x in nums if x > 1])

print(mayores)

def hay_par(nums):
    i = 0
    while True:
        if i >= len(nums):
            break
        if nums[i] % 2 == 0:
            break
        i+=1
    return i < len(nums)


print(hay_par(nums))

