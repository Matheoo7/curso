# Planteo Ejercicio en Clase: 

# Determinar y mostrar la calificación de un estudiante según la nota: 

# Si la nota es mayor o igual a 9 deberá imprimir "Excelente"
# Si la nota es mayor o igual a 7 debera imprimir "Muy bueno"
# Si la nota es mayor o igual a 4 debera imprimir "Bueno"
# Si la nota es menor a 4 debera imprimir "Desaprobado"

nota = 7 

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muy bueno")
elif nota >= 4:
    print("Bueno")
else:
    print("Desaprobado")

# Cualquiera sea la nota primero debera de pasar en orden por cada una de las condiciones y luego imprimir el resultado correspondiente. (ej. si pongo 8 no imprimira "Bueno", ya que paso por la condicion de "Muy bueno")