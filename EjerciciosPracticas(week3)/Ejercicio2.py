# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número

numero = int(input("Ingrese un numero positivo: "))
total = 0

for num in range (1,numero):
    total += num

print(total)