numeroOblongo = lambda x: any(n*(n+1)==x for n in range(1,x))

if numeroOblongo(90):
    print("Es oblongo!")
else:
    print("No es oblongo!")

numeroTriangular = lambda x: any((n*(n+1))/2==x for n in range(1,x))

if numeroTriangular(6):
    print("Es triangular!")
else:
    print("No es triangular!")