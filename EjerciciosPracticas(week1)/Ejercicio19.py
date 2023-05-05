numero = float(input("Ingrese un numero decimal: "))

entero = int(numero)
decimal = float(round(numero-entero,2)) # funciona pero te redondea si hay mas de 2 decimales
print(f"La parte entera es:", entero, "|", "La parte decimal es:", decimal)