
palabra = input("Ingrese una palabra: ")

palabra_reversa = palabra[::-1]

if palabra == palabra_reversa:
    print("Es palindromo")
else:
    print("No es palindromo")