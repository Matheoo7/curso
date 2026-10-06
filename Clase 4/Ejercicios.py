nombre = input("Ingrese su nombre: ").lower().title()
apellido = input("Ingrese su apellido: ").lower().title()
email = input("Ingrese correo electronico: ")
edad = int(input("Ingrese su edad: "))

print("\nNombre completo:", nombre, apellido)

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