texto = "PyThOn"
print(texto.lower())
# Resultado: "python"

nombre = "María JOSÉ"
print(nombre.lower())
# Resultado: "maría josé"

texto = "Hola Mundo"   
print(texto.upper())
# Salida: HOLA MUNDO

texto = "   Camino    "
print(texto.strip())
# Salida: Camino

texto = "Hola Mundo"   
print(texto.replace("Mundo", "Python"))
# Salida: Hola Python

texto = "Hola Mundo"   
print(texto.startswith("Hola"))
# Salida: True

texto = "Hola Mundo"   
print(texto.endswith("Mundo"))
# Salida: True

texto = "Hola Mundo"   
print(texto.find("Mundo"))
# Salida: 5

texto = "123"   
print(texto.isdigit())
# Salida: True