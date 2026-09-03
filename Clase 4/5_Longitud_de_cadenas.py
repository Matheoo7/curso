palabra = "Edificio"

print(palabra)

# [0 al 9] Pone la letra en la posición 0 de "Edificio" (E)

primera_palabra = palabra[0]
print(primera_palabra)

# [0 al 9] Pone la letra en la posicion 4 de "Edificio" (I)

letra_al_azar = palabra[4]
print(letra_al_azar)

# Len: Cantidad de caracteres de un texto o palabra

longitud = len(palabra)
print(longitud)

# Ejemplo len

mensaje = input("Ingresar un mensaje: ")

print("La longitud del mensaje es de " + str(len(mensaje)) + "caracteres")