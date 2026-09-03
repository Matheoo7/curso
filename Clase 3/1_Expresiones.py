# Una expresión es una relación entre dos operandos y un operador

# Expresión aritmética: el operador puede ser +, -, *, /, //, %

num1 = 3
num2 = 5

suma = num1 * num2 

print(suma)

# Expresion comparativa o racional: operadores ==, >, >=, <, <=, !=

#  == : Igual que               != : No igual que
#   > : Mayor que                < : Menor que
#  >= : Mayor o igual que       <= : Menor o igual que

# Las expresiones comparativas siempre tienen por resultado un valor booleano (True/False)

print(3 > 4)             # False
print(2 <= 4)            # True
print(2 != 22)           # True
print("Hola" == "hola")  # False
print("Carlos" < "Ada")  # False

# Expresión lógica: operadores son el "and", "or", "not"

# and(Y): Devuelve True si todas las condiciones son verdaderas
# or(O): Devuelve True si al menos una condición es verdadera
# not(No): Invierte el valor de verdad de una expresión

a = 10
b = 14

print(a < 10 or b == 14)
print(b < a and b == b)