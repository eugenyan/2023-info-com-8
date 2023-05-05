# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.

txt = input("Ingrese un parrafo o una frase: ")

# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.

#letra1, letra2, letra3 = input("Ingrese la una letra a eleccion: "), input("Ingrese la otra letra a eleccion: "), input("Ingrese una ultima letra a eleccion: ")
#o
letra1 = input("Ingresa una letra eleccion: ")
letra2 = input("Ingrese otra letra a eleccion: ")
letra3 = input("Ingrese una ultima letra a eleccion: ")

# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string

letras = [letra1.lower(), letra2.lower(), letra3.lower()]

# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula

txt = txt.lower()
for letra in letras:
    print(f'La letra {letra} aparecio {txt.count(letra)} veces')

# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud

palabras = txt.replace('.', '')
palabras = palabras.replace(':', '')
palabras = palabras.replace(';', '')
palabras_sep = palabras.split(' ')
print("Palabras sin caracteres de puntuacion:", palabras)

cant_palabras = len(palabras_sep)
print("Cantidad de palabras en el texto:", cant_palabras)

# 3- Cual es la primera letra y cuál es la última. (Indexación)

print("Primera letra:", palabras[0], "Ultima letra:", palabras[-1])

# 4- Mostrar el texto en orden inverso

txt_reversa = palabras[::-1]
print("Texto al reves:", txt_reversa)

palabras_reversa = palabras_sep[::-1]
print("Palabras al reves:", palabras_reversa)

txt_palabras_reversa = " ".join(palabras_reversa)
print("Palabras en forma inversa como string:", txt_palabras_reversa)

# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario.

opciones = {True: "existe", False: "no existe"}
existe_python = "python" in txt

print("La palabra python", opciones[existe_python])