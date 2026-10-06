print("\nBienvenido a nuestro Banco Finar\n")

print("1. Consultas")
print("2. Extraccion")
print("3. Transferir")
print("4. Depositar")
print("5. Imprimir comprobante")
print("6. Cerrar sesion")

opcion = int(input("\nIngrese la opcion deseada: "))

while opcion != 6:
    if opcion == 1:
      print("Consultando...")
    elif opcion == 2:
      print("Extrayendo...")
    elif opcion == 3:
      print("Transfiriendo...")
    elif opcion == 4:
      print("Depositando...")
    elif opcion == 5:
      print("Imprimiendo..")
    elif opcion == 6:
      print("Cerrando sesion..")
    else: 
      print("Opcion invalida")

    print("\nBienvenido a nuestro Banco Finar\n")

    print("1. Consultas")
    print("2. Extraccion")
    print("3. Transferir")
    print("4. Depositar")
    print("5. Imprimir comprobante")
    print("6. Cerrar sesion")

    opcion = int(input("\nIngrese la opcion deseada: "))

print("Sesion cerrada con exito.")