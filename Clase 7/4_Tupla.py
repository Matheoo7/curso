# Una tupla se crea poniendo parentesis en una lista y tienen como caracteristica que son inmutables, al contrario que las listas
dias_de_la_semana = ("Lunes","Martes","Miercoles","Jueves","Viernes")

print(dias_de_la_semana[0])

# tuple() se usa para convertir una lista a una tupla
mi_lista = [1, 2, 3]
mi_tupla = tuple(mi_lista)
print(mi_tupla)  # Salida: (1, 2, 3)

# list() se usa para convertir una tupla a una lista
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)  # Salida: [4, 5, 6]

# Índices positivos: Acceden desde el principio
#Índices negativos: Acceden desde el final
colores = ("rojo", "verde", "azul")

print(colores[0]) # Salida: rojo

print(colores[-1]) # Salida: azul