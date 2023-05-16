

frase = input("Escriba una frase: ")

palabras = frase.replace('.', '')
palabras = palabras.replace(':', '')
palabras = palabras.replace(';', '')
palabras = palabras.replace(',', '')
palabras_sep = palabras.split(' ')

print(len(palabras_sep))