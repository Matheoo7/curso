""" Intentá que si algún dato no es válido, **el programa muestre cuál fue el problema** (en lugar de solo "ERROR!").

Por ejemplo:
- “La edad debe ser mayor a 18.”
- “El correo no puede estar vacío.” """

print("-----Sus datos-----")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
email = input("Correo electrico: ")
print("-------------------")

if nombre == "" or apellido == "" or edad < 18 or email == "":
    print("\n-Error!-")

if nombre == "" or apellido == "":
    print("Falta completar")
else:
    print("Nombre completo:", nombre, apellido)

if edad < 18:
    print("Debe ser mayor de edad")
else:
    print("Es mayor de edad")

if email == "":
    print("Falta completar")
else:
    print("Correo electronico:", email)

# Necesito que cuando haya algun error, solo se muestre el mensaje de cual fue el problema y no se vea los datos ingresados correctamente

