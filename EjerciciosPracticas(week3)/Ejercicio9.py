
numero = int(input("Ingrese un numero: "))
cont = 0
fib = [0, 1, 1, 2]
while True:
    suma_ant = fib[-2] + fib[-1]
    if(suma_ant > numero):
        print("El numero anterior de la secuencia de Fib a ese num es:", fib[-1])
    elif(suma_ant == numero):
        print("El numero de la secuencia de Fib correspondiente a ese num es:", suma_ant)
        break
    else:
        fib.append(suma_ant)


