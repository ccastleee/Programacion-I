def validarNota(lista):
    nota = int(input("Ingrese: "))
    while nota != -1:
        while nota < 0 or nota > 10:
            print("Solo notas entre 0 y 10!")
            nota = int(input("Ingrese: "))
        if nota != -1:
            lista.append(nota)
        nota = int(input("Ingrese: "))
    return lista
    

def main():
    listaCursos = []
    print("Ingrese las notas del curso.")
    listaCursos = validarNota(listaCursos)
    print(listaCursos)

main()