"""Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma."""

class menorCero(Exception):
    pass

def validarNumeroNatural():
    try:
        num = int(input("Ingrese un numero natural: "))
        if num <= 0:
            raise menorCero
        #assert num > 0, "Error, menor a 0"
    except ValueError:
        print("Error, ingrese un numero valido.")
    except menorCero:
        print("Error, numero menor a 0.")
    else:
        print(f"El numero ingresado es {num}.")

validarNumeroNatural()