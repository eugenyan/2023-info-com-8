# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.

letra = input("Ingrese una letra random: ")
vocales = ["a", "e", "i", "o", "u"]

if letra in vocales:
    print("Es VOCAL")
else:
    print("Es CONSONANTE")