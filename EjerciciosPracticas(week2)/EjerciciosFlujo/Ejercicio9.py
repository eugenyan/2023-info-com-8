
mayor = 0
maximo = 3
 
for i in range(maximo):
    num = int(input("Ingrese un numero:"))
    if num > mayor:
        mayor = num
 
print(mayor)