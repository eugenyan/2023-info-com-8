from random import randint
# import random

# Pedir al usuario que ingrese su nombre.
nombre = input("Ingrese su nombre: ")

# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
print("｡.:* Bienvenidx,", nombre, "! *.:｡\nVoy a elegir un numero del 1 al 100, \ny tenés 8 intentos para adivinar cuál es...")

# Generar aleatoriamente un número entero entre 1 y 100.
random_num = randint(1, 100)
intentos = 0

while True:
    numero = int(input("☘ Probá tu suerte: "))
    intentos =+ 1
    if (numero > random_num):
        print("Te pasaste! Intena con un numero menor ;)")
        print(f"Intenta nuevamuente. Te quedan {8 - intentos} intentos")
    elif (numero < random_num):
        print("Estas lejos! Intenta con un numero mayor ;)")
        print(f"Intenta nuevamente. Te quedan {8 - intentos} intentos")
    elif (intentos == 8):
        print("(ಥ︹ಥ) MALA SUERTE! Tuviste muchos intentos.")
        print("El numero era:", random_num)
        break
    else:
        print("٩〔^ᴗ^〕۶ ACERTASTE!")
        print("Te tomó", intentos, "intentos.")
        break


# (es_int == False):
#         print("⊰(Ŏ ⋓ Ŏ)⊱ Ups! Ese no era un numero entero...")

# while cont_intentos < 8:
#      print("Todavia intentos", 8 - (cont_intentos + 1))
#      cont_intentos += 1


# El "número" ingresado por el usuario puede:
#  No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
# tip 2: con el método isdigit() puedes saber si es posible convertir a entero
#  Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
#  Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
#  Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento
# lo adivinó.
#  Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si
# debes descontarle un intento.
#  En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que
# ingrese otro número.
#  Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el
# número que tenía que adivinar.