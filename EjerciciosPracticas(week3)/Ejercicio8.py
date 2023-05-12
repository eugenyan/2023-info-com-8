# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.

frase = input("Escriba una frase: ")

palabras = frase.replace('.', '')
palabras = palabras.replace(':', '')
palabras = palabras.replace(';', '')
palabras = palabras.replace(',', '')
palabras_sep = palabras.split(' ')

print(len(palabras_sep))