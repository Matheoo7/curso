# Planteo: hacer un programa que permita el ingreso a una plataforma, solicitando una clave, con solo 3 intentos posibles.

intentos = 1
verificado = False

while intentos <= 3:
    clave = input("Ingrese la contraseña: ")

    if clave == "1234":
        print("Bienvenido, usuario!")
        verificado = True
        break
    else:
        print("Contraseña incorrecta")
    intentos = intentos + 1

if verificado == False:
    print("Tarjeta cancelada")