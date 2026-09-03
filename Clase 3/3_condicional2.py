# Ejemplo que muestra si una persona al ingresar su edad, es mayor de edad o no

edad = int(input("Ingrese su edad: "))

if edad >= 18: 
    print("Es mayor de edad")
else: 
    print("Es menor de edad")

# Ejemplo indica si una persona puede votar o no. Para ello debe ser mayor o igual de 18 y ser ciudadano

    edad = 20
es_ciudadano = True
if edad >= 18 and es_ciudadano:
    print("Podés votar.")
else:
    print("No podés votar.")