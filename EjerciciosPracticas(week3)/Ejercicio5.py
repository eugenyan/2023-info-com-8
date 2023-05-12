# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al
# 100.
suma_par = 0

for num in range (1,101):
    if (num % 2 == 0):
        suma_par += num

print(suma_par)