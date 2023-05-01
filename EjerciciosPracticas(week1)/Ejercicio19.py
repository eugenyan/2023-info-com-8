numero = float(input("Ingrese un numero decimal: "))

entero = int(numero)
decimal = float(round(numero-entero,2))
print(f"La parte entera es:", entero, "|", "La parte decimal es:", decimal)