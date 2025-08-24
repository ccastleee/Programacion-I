def devolverMayor(a,b,c):
    encontrado = False
    if a > b:
        if a > c:
            print(a)
            encontrado = True
    if b > a:
        if b > c:
            print(b)
            encontrado = True
    if c > a:
        if c > b:
            print(c)
            encontrado = True
    if encontrado == False:
        print(-1)
    
def mostrarMaximo():
    encontrado = False
    print("Ingrese 3 valores")
    a = int(input("Ingrese: "))
    b = int(input("Ingrese: "))
    c = int(input("Ingrese: "))
    if a > b:
        if a > c:
            print(a)
            encontrado = True
    if b > a:
        if b > c:
            print(b)
            encontrado = True
    if c > a:
        if c > b:
            print(c)
            encontrado = True
    if encontrado == False:
        print("No hay un maximo!")

devolverMayor(2,2,2)
mostrarMaximo() 