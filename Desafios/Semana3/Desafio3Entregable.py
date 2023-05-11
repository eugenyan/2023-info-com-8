from random import randint
# import random

# Pedir al usuario que ingrese su nombre.
nombre = input("Ingrese su nombre: ")

# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
print("｡.:* Bienvenidx,", nombre, "! *.:｡\nVoy a elegir un numero del 1 al 100, \ny tenés 8 intentos para adivinar cuál es...")

# Generar aleatoriamente un número entero entre 1 y 100.
random_num = randint(1, 10)
intentos = 0

while True:
    numero = (input("☘ Probá tu suerte: ")) # Solicitarle que ingrese un número.
    es_int = numero.isdigit()
    intentos += 1
    if es_int == False:
        intentos -= 1 # Si el usuario no ingresa un número entero no debes descontarle un intento
        print("⊰(Ŏ ⋓ Ŏ)⊱ Ups! Ese no era un numero entero...") # avisarle que no es un número entero el que ingresó.
    elif (intentos == 8):
        print("(ಥ︹ಥ) MALA SUERTE! Tuviste muchos intentos.") # debes informarle que se agotaron los intentos 
        print("El numero era:", random_num) # cuál era el número que tenía que adivinar.
        break
    elif es_int < random_num and es_int == True:
        print("Estas lejos! Intenta con un numero mayor ;)") # informarle que el número a adivinar es mayor.
        print(f"Intenta nuevamente. Te quedan {8 - intentos} intentos") # Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
    elif es_int > random_num and es_int == True:
        print("Te pasaste! Intena con un numero menor ;)") # informarle que el número a adivinar es menor.
        print(f"Intenta nuevamuente. Te quedan {8 - intentos} intentos") # Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
    else:
        es_int == random_num
        print("٩〔^ᴗ^〕۶ ACERTASTE!") # informarle que ha ganado 
        print("Te tomó", intentos, "intentos.") # decirle en cuál intento lo adivinó.
        break