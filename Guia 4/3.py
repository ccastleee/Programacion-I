"""Los números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89."""

def descifrarClaveMap(clave):
    lista = ','.join(clave).split(',')
    listaClave = list(map(int, lista))
    impares = [str(listaClave[p]) for p in range(len(listaClave)) if p % 2 != 0]
    pares = [str(listaClave[p]) for p in range(len(listaClave)) if p % 2 == 0]
    claveImpar, clavePar = ''.join(impares), ''.join(pares)
    return clavePar, claveImpar

def descifrarClave(clave):
    impares = []
    pares = []
    for i in range(len(clave)):
        if i % 2 != 0:
            impares.append(clave[i])
        else:
            pares.append(clave[i])
    clavePar, claveImpar = ''.join(pares), ''.join(impares)
    return clavePar, claveImpar

def main1():
    claveMaestra = "92302"
    clavePar, claveImpar = descifrarClaveMap(claveMaestra)
    print(f"Funcion con map y list\nClave 1: {clavePar}, Clave 2: {claveImpar}")

def main2():
    claveMaestra = "92302"
    clavePar, claveImpar = descifrarClave(claveMaestra)
    print(f"Funcion basica\nClave 1: {clavePar}, Clave 2: {claveImpar}")

main1()
main2()