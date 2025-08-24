a,b = int(input("Ingrese el numero A: ")),int(input("Ingrese el numero B: "))

lista = [x for x in range(a,b+1) if (x % 7 == 0 and x % 5 != 0)]
print(lista)