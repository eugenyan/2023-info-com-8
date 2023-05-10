# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input("Ingrese un caracter: ")

if (caracter.isalpha()):
    print("Es LETRA")
    if (caracter.islower()):
        print("es minuscula")
    else:
        print("ES MAYUSCULA")
elif (caracter.isdigit()):
    print("Es NUM3R0")
else:
    print("Es un caracter *+.° especial *+.° ")