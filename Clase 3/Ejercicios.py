print("-----Sus datos-----")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
email = input("Correo electrico: ")
print("-------------------")

if nombre == "" or apellido == "" or edad < 18 or email == "":
    print("--ERROR--")
else:
    print("\n--Datos ingresados--")
    print("Nombre completo:", nombre, apellido)
    print("Correo electronico:", email)
    print("Es mayor de edad")
    print("-------------------") 