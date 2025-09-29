alumnos = {1221635: "Melani Ayelen Castillo", 1221636: "ABC", 1221635: "Matias Leonel Castillo"}

for legajo,alumno in alumnos.items():
    print(f"{legajo}, {alumno}")

print(alumnos.get(1221635, "No existe el numero de legajo."))
print(alumnos.get(1221637, "No existe el numero de legajo."))

