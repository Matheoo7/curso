# append() agrega un elemento al final de la lista.
ventas = [190, 25, 38]
ventas.append(101) # Salida: [190, 25, 38, 101]

# remove() elimina la primera aparición de un valor.
productos = ["pan", "leche", "queso"]
productos.remove("pan")
print(productos) # Salida: ["leche", "queso"]

# clear() elimina todos sus elementos, dejando una lista vacía
mi_lista = [1, 2, 3, 4, 5]
mi_lista.clear()
print(mi_lista) # salida: []

# pop() elimina un elemento y lo deja guardado para poder devolverlo. Si no se especifica el elemento a eliminar se elimina el ultimo
frutas = ["manzana", "banana", "cereza", "naranja"]
elemento_eliminado = frutas.pop()
print(frutas) # Salida: ["manzana", "banana", "cereza"]
print(elemento_eliminado) # Salida: naranja

# instert() inserta un elemento en una posición específica.
fruits = ["camion", "camioneta", "moto"]
fruits.insert(1, "auto") # Salida: ["camion", "auto", "camioneta", "moto"]

# count() cuenta cuántas veces aparece un valor en la lista.
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry") # Salida: 1

# extend() añade elementos de otra lista o iterable al final.
fruits = ['apple', 'banana', 'cherry']
autos = ['Ford', 'BMW', 'Volvo']
fruits.extend(autos) # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# index() devuelve la posición de la primera aparición de un valor.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry") # Salida 2

# sort() ordena los elementos de la lista.
autos = ['Ford', 'BMW', 'Volvo']
autos.sort() # Salida: ['BMW', 'Ford', 'Volvo']