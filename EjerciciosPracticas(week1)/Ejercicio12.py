import datetime
fecha_nac = input('Ingrese su fecha de nacimiento (dd/mm/aaaa): ')
dia, mes, anio = map(int, fecha_nac.split('/'))

fecha_act = datetime.date.today()
anio_hoy = fecha_act.year
mes_hoy = fecha_act.month
dia_hoy = fecha_act.day
edad = anio_hoy - anio
if((mes == mes_hoy) and (dia == dia_hoy)):
    print("Feliz cumple!", edad, "pirulos")
elif((mes == mes_hoy) and (dia < dia_hoy)):
    print("Tu edad actual es de ", edad, " años")
elif((mes == mes_hoy) and (dia <= dia_hoy+3)):
    print("Falta poco para tu cumple ;)", edad, " años")
else:
    (mes > mes_hoy)
    print("Tu edad actual es de ", edad," años")