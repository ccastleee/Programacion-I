def cantidadViajesMes(gasto, cantViajes):
    if 1>=cantViajes<=20:
        porcentaje = 10
    elif 21>=cantViajes<=30:
        porcentaje = 20
    elif 31<=cantViajes<=40:
        porcentaje = 30
    else:
        porcentaje = 40
    descuento = round((gasto*porcentaje/100), 2)
    return porcentaje, descuento

def main():
    porcentaje, descuento = cantidadViajesMes(275.45, 45)
    print(f"Se aplica un total de {porcentaje}% de descuento.\nTotal ahorrado: {descuento}$")

main()