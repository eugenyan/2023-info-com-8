# print("Hola", "que", sep='-', end="...\n") # por default sep=" " end="\n"
# print("Hola2") # \n salto de linea
# print("Hola3",) 

#Como hacer mas prolijo un codigo? Modularizacion
#Que usar cuando se repiten cosas? Modularizacion
#Que formas de modularizar existen? Funciones y Procedimientos
#Que hace una funcion? Realiza Ncant. acciones -> devuelve un valor. Ej f(x) -> f(3) = 5
#Que hace un procedimiento? Realiza Ncant. acciones

# def nombre_funcion(param1, param2, param3):
#     pass

# def funcion(x, y, z):
#     pass

# def funcion (x, y):
#     pass

# 19-Escribe un programa que pida al usuario un número y luego imprima si ese
# número es un número perfecto o no. Un número perfecto es aquel que es igual a
# la suma de sus divisores propios (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
# puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

def perfecto(num): # 6. 1, 2, 3
    divisores = []
    for n in range(1,num):
        if(num % n == 0):
            divisores.append(n)

    if(num==suma(divisores)):
        print("Es perfecto.")
    else:
        print("No es perfecto.")

def suma(nums_lista):
    suma_lista = 0
    for n in nums_lista:
        suma_lista += n

    return suma_lista

perfecto(int(input("Ingrese su numero")))