
txt = input("Ingrese una frase: ")
txt_vocales = " "

for letra in txt:
    if letra in ('a', 'e', 'i', 'o', 'u'):
        letra = letra.upper()
        txt_vocales += letra
    else: 
        txt_vocales += letra

print(txt_vocales)
 