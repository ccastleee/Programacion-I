def calcularVuelto(total, recibido):
    cambio = recibido - total
    if recibido < total:
        print("Error, total insuficiente.")
    if cambio == 0:
        print("No hay vuelto.")
    b5000 = cambio // 5000
    cambio %= 5000
    b1000 = cambio // 1000
    cambio %= 1000
    b500 = cambio // 500
    cambio %= 500
    b200 = cambio // 200
    cambio %= 200
    b100 = cambio // 100
    cambio %= 100
    b50 = cambio // 50
    cambio %= 50
    b10 = cambio // 10
    cambio %= 10
    if cambio != 0:
        print("No es posible entregar el cambio.")
    else:
        print("Vuelto:")
        if b5000 > 0:
            print(f"{b5000} billete(s) de $5000.")
        if b1000 > 0:
            print(f"{b1000} billete(s) de $1000.")
        if b500 > 0:
            print(f"{b500} billete(s) de $500.")
        if b200 > 0:
            print(f"{b200} billete(s) de $200.")
        if b100 > 0:
            print(f"{b100} billete(s) de $100.")
        if b50 > 0:
            print(f"{b50} billete(s) de $50.")
        if b10 > 0:
            print(f"{b10} billete(s) de $10.")

total = int(input("Total a pagar: "))
recibido = int(input("Total recibido: "))
calcularVuelto(total, recibido)
        




