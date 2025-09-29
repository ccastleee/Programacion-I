"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C."""


def confirmacionUsuario():
    confirmar = input("Desea interrumpir el programa (s/n): ").lower()
    return confirmar

def numeros10000():
    i = 0
    while True:
        try:
            while i <= 100000:
                print(i)
                i+=1
        except KeyboardInterrupt:
            if confirmacionUsuario() == "s":
                break
            else:
                continue

def main():
    numeros10000()

main()