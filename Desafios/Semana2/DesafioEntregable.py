txt = input("Ingresa un párrafo o una frase: ")
letra1 = input("Ingresa una letra elección: ")
letra2 = input("Ingresa otra letra a elección: ")
letra3 = input("Ingresa una última letra a elección: ")

letras = [letra1.lower(), letra2.lower(), letra3.lower()]
txt = txt.lower()

for letra in letras:
    print(f'La letra {letra} apareció {txt.count(letra)} veces')

palabras = txt.replace('.', '')
palabras = palabras.replace(':', '')
palabras = palabras.replace(';', '')
palabras = palabras.replace(',', '')
palabras_sep = palabras.split(' ')
print("Palabras sin caracteres de puntuación:", palabras)

cant_palabras = len(palabras_sep)
print("Cantidad de palabras en el texto:", cant_palabras)

print("Primera letra:", palabras[0],"|", "Última letra:", palabras[-1])

txt_reversa = palabras[::-1]
print("Texto al revés:", txt_reversa)

opciones = {True: "EXISTE", False: "NO EXISTE"}
existe_python = "python" in txt
print("La palabra python", opciones[existe_python])