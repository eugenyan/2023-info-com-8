# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
# la suma de ellos solo si ambos son pares.

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("La suma da:", num1 + num2)
else:
    print("No se me permite sumar esos dos numeros :(")