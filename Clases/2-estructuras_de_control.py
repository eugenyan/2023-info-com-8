# estructuras condicionales
# manejar el flujo de actividades tareas que voy a realizar con mi algoritmo

# ... codigo, condicional simple
a = 5
b = 10

if(a==b): # si pasa esto, hace lo que esta debajo
    print("b y a son iguales")

else: # si no pasa lo de arriba hace esto
    print("b y a NO son iguales")

# condicional multiple
if(a==b):
    print("b y a son iguales")
elif(a*3==30):
    print("a es igual a 10")
elif(a/20==10):
    print("")
else:
    print("")

# estructuras repetitivas
# con contador, con condicional a priori, con condicional posteriori

for X in range(1,10):
    print(X)

for X in "hola como estas":
    print(X)

while(a!=10):
    print(a) # para cortar un programa que no para, se usa: CTRL+C
    a += 1


