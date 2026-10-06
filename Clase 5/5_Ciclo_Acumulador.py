# Hacer un programa en el que el usuario ingrese numeros enteros, y finalice la carga ingresando el numero cero. Al concluir el programa deberá mostrar la suma total de los numeros ingresados.


# Suma total guarda y suma los numeros ingresados en num en cada ciclo
suma_total = 0

# En num se imprimen los numeros que ingresa el usuario.
num = int(input("Ingrese un numero entero: "))

# La cont se suma + 1 a si mismo para contar la CANTIDAD de veces que el ciclo pasa por el.
cont = 0

# Mientras que el numero ingresado en num no sea igual (!=) a 0, se sigue ejecutando el bucle. Si se ingresa el 0, el bucle termina y sigue imprimiendo lo que este aparte del while
while num != 0:
    cont = cont + 1
    suma_total = suma_total + num
    num = int(input("Ingrese un numero entero: "))

promedio = suma_total / cont

print(f"Cantidad de numeros ingresados: {cont}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio}")