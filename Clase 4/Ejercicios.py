# Se usa .lower() para poner toda la palabra en minuscula y .title() para poner la primera letra de la palabra en mayuscula

nombre = input("Ingrese su nombre: ").lower().title()
apellido = input("Ingrese su apellido: ").lower().title()
email = input("Ingrese correo electronico: ")
edad = int(input("Ingrese su edad: "))

print("\nNombre completo:", nombre, apellido)

# .count cuenta la cantidad de los caracteres que pongas en el (). Puse not ... == 1 para que entienda que si la cantidad de los caracteres que puse en el () NO es igual a == 1, imprima "Error!"

if " " in email:
    print("Error!")
elif not email.count("@") == 1:
    print("Error!")
else:
    print("Correo electronico:", email)

if edad < 15:
    print("Es un/a niño/a")
elif edad >= 15:
    print("Es un adolecente")
elif edad > 18:
    print("Es un/a adulto/a")