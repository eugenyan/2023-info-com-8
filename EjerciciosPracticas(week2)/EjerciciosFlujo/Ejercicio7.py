
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