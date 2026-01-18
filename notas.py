notas = []
cantidad = int(input("¿Cuántos estudiantes hay? "))

for i in range(cantidad):
    nota = float(input(f"Ingresá la nota del estudiante {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("Notas ingresadas:", notas)
print("Promedio:", promedio)

if promedio >= 6:
    print("Estado: Aprobado")
else:
    print("Estado: Desaprobado")
