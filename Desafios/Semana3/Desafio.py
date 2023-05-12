# import random
from random import randint

# Pedir al usuario que ingrese su nombre.
nombre = input("Ingrese su nombre: ")

# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
print("\n｡.:* Bienvenidx,", nombre, "! *.:｡\nVoy a elegir un numero del 1 al 100, \ny tenés 8 intentos para adivinar cuál es...\n")

# Generar aleatoriamente un número entero entre 1 y 100.
random_num = randint(1, 100)
intentos = 0

while intentos < 8:
    numero = (input("☘ Probá tu suerte: ")) # # # # Solicitarle que ingrese un número.
    if (numero.isdigit() == False):
        print("\n⊰(Ŏ ⋓ Ŏ)⊱ Ups! Ese no era un numero entero...\n") # # # # avisarle que no es un número entero el que ingresó.
        continue

    intentos += 1
    es_int = int(numero)

    if (es_int > random_num):
        print("\nTe pasaste! Intena con un numero menor ;)") # # # # informarle que el número a adivinar es menor.
        print(f"Intenta nuevamuente. Te quedan {8 - intentos} intentos.\n") # # # # Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
    elif (es_int < random_num):
        print("\nEstas lejos! Intenta con un numero mayor ;)") # # # # informarle que el número a adivinar es mayor.
        print(f"Intenta nuevamente. Te quedan {8 - intentos} intentos.\n") # # # # Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
    else:
        (es_int == random_num)
        print("\n ٩〔^ᴗ^〕۶ ACERTASTE!") # # # # informarle que ha ganado 
        print("  Te tomó", intentos, "intentos.") # # # # decirle en cuál intento lo adivinó.
        break
else:
    (intentos == 8)
    print("\n(ಥ︹ಥ) MALA SUERTE! Tuviste muchos intentos.") # # # # debes informarle que se agotaron los intentos
    print("El numero era:", random_num) # # # # cuál era el número que tenía que adivinar.