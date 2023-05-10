
txt = input("Ingrese una frase: ")

opciones = {True : "CONTIENE", False : "NO Contiene"}
contiene_a = "a" in txt
print("La frase elegida", opciones[contiene_a], "a")
