# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
# el mayor de ellos.

mayor = 0
maximo = 3
 
for i in range(maximo):
    num = int(input("Ingrese un numero:"))
    if num > mayor:
        mayor = num
 
print(mayor)