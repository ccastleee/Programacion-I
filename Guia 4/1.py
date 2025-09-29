"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento."""

def esCapicua(cadena):
    capicua = ""
    for i in range(len(cadena)//2):
        if cadena[i] != cadena[-(i+1)]:
            capicua = "no es capicua!"
        else:
            capicua = "es capicua!"
    return capicua

palabra = "Ada".lower()
print(f"La palabra {esCapicua(palabra)}")