# Desarrolla un algoritmo que solicite al usuario el ingreso de un número del 1 al 4, e imprima ese numero en letras.
# Si el usuario ingresa 

num = int(input("Ingrese un número del 1 al 4: "))

""" if num == 1:
    print("Uno")
elif num == 2:
    print("Dos")
elif num == 3:
    print("Tres")
elif num == 4:
    print("Cuatro")
else:
    print("Número inválido") """


match num:
    case 1:  print("uno")
    case 2:  print("dos")
    case 3:  print("tres")
    case 4:  print("cuatro")
    case _:  print("Número inválido")