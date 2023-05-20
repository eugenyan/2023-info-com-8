# Lista de inmuebles
inmuebles = [{'anio': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
             {'anio': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
             {'anio': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
             {'anio': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
             {'anio': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


# Tenemos Reglas de Validacion
def validacion(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:  # Inmuebles solo de zona: A, B o C.
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:  # Inmuebles con estado: Disponible, Reservado o Vendido.
        return False
    if inmueble['anio'] < 2000:  # No opera con inmuebles anteriores al año 2000.
        return False
    if inmueble['metros'] < 60:  # No opera con inmuebles menores de 60 metros cuadrados.
        return False
    if inmueble['habitaciones'] < 2:  # No opera con inmuebles menores de 2 habitaciones.
        return False

    return True


# Tenemos Reglas de Precio
def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['anio']
    precio_base = inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500

    if inmueble['zona'] == 'A':
        precio = precio_base * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = precio_base * (1 - antiguedad / 100) * 1.5
    elif inmueble['zona'] == 'C':
        precio = precio_base * (1 - antiguedad / 100) * 2
    else:
        precio = None # Para cuando no pasa la validacion

    return precio


# 1
def agregar_inmueble():
    inmueble = {}

    inmueble['anio'] = int(input('Año: '))
    inmueble['metros'] = int(input('Mts2: '))
    inmueble['habitaciones'] = int(input('Cantidad de habitaciones: '))
    inmueble['garaje'] = input('Garaje SI/NO: ').upper() == 'SI'
    inmueble['zona'] = input('Zona A, B o C: ').upper()
    inmueble['estado'] = input('Estado Disponible, Reservado o Vendido: ').capitalize()
    inmueble['precio'] = calcular_precio(inmueble)

    if validacion(inmueble):
        if inmueble['precio'] is not None:
            inmuebles.append(inmueble)
            print('Se agregó el inmueble satisfactoriamente.')
        else:
            print('El inmueble no cumple con las reglas de validación.')
    else:
        print('El inmueble no cumple con las reglas de validación.')


# 2
def editar_inmueble(inmuebles, index):
    if index >= 0 and index < len(inmuebles):
        inmueble = inmuebles[index]
        inmueble_editado = dict(inmueble)

        inmueble_editado['anio'] = int(input('Año: '))
        inmueble_editado['metros'] = int(input('Mts2: '))
        inmueble_editado['habitaciones'] = int(input('Cantidad de habitaciones: '))
        inmueble_editado['garaje'] = input('Garaje SI/NO: ').upper() == 'SI'
        inmueble_editado['zona'] = input('Zona A, B o C: ').upper()
        inmueble_editado['estado'] = input('Estado Disponible, Reservado o Vendido: ').capitalize()

        if validacion(inmueble_editado):
            inmueble_editado['precio'] = calcular_precio(inmueble_editado)
            inmuebles[index] = inmueble_editado
            print('Cambios guardados exitosamente.')
        else:
            print('El inmueble editado no cumple con las reglas de validación.')
    else:
        print('El índice del inmueble no es válido.')


# 3
def borrar_inmueble(inmuebles, index):
    if index >= 0 and index < len(inmuebles):
        del inmuebles[index - 1]
        print('Se ha eliminado el inmueble exitosamente.')
    else:
        print('El índice del inmueble no es válido.')


# 4
def buscar_inmueble(inmuebles, presupuesto):
    resultado_busqueda = []
    precio_mas_barato = float('inf')  # Inicializamos con un valor infinito

    for inmueble_actual in inmuebles:
        precio = inmueble_actual.get('precio', 0)

        if precio < presupuesto and inmueble_actual['estado'] in ['Disponible', 'Reservado']:
            copia_inmueble = dict(inmueble_actual)
            copia_inmueble['precio'] = calcular_precio(inmueble_actual)
            resultado_busqueda.append(copia_inmueble)

            # Actualizamos el precio más barato si corresponde por si buscamos presupuestos más bajos y no existen
            if precio < precio_mas_barato:
                precio_mas_barato = precio

    if not resultado_busqueda:
        print('No se encontraron inmuebles que cumplan con el presupuesto.')
    elif presupuesto > precio_mas_barato:
        print('El presupuesto ingresado es menor que el precio del inmueble más barato.')

    return resultado_busqueda


# 5
def mostrar_inmuebles(inmuebles):
    cont = 1
    for inmueble in inmuebles:
        print(f"\n░░░░░░ INMUEBLE {cont} ░░░░░░")
        print('Año:', inmueble['anio'])
        print('Metros cuadrados:', inmueble['metros'])
        print('Número de habitaciones:', inmueble['habitaciones'])
        print('¿Tiene garaje?:', "Sí" if inmueble['garaje'] else "No")
        print('Zona:', inmueble['zona'])
        print('Estado:', inmueble['estado'])
        print('Precio:', calcular_precio(inmueble))
        cont += 1


# ===================== Programa

usuario = input('Ingresa tu usuario: ')

while usuario:
    print("\n░░░░░░ MENU ░░░░░░")
    print("\n1. Agregar inmueble")
    print("2. Editar inmueble")
    print("3. Eliminar inmueble")
    print("4. Búsqueda de inmuebles por presupuesto")
    print("5. Mostrar Inmuebles")
    opcion = input(f"\nBienvenido {usuario}!\nElige una opción del menú: ")
    
    if opcion == '1':
        agregar_inmueble()
    elif opcion == '2':
        index = int(input('Ingresa el índice del inmueble a editar: '))
        editar_inmueble(inmuebles, index)
    elif opcion == '3':
        index = int(input('Ingresa el índice del inmueble a eliminar: '))
        borrar_inmueble(inmuebles, index)
    elif opcion == '4':
        presupuesto = float(input('Ingresa el presupuesto máximo: '))
        encontrados = buscar_inmueble(inmuebles, presupuesto)
        if encontrados:
            print(f"Se encontraron {len(encontrados)} inmuebles:")
            mostrar_inmuebles(encontrados)
    elif opcion == '5':
        mostrar_inmuebles(inmuebles)
    else:
        print('Opción no válida.')

    usuario = input('\nIngresa tu usuario (o presiona Enter para salir): ')

