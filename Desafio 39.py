from datetime import datetime

# Se le pide al usuario que ingrese las dos fechas
fecha1 = input("Ingrese la primera fecha (dd/mm/aaaa): ")
fecha2 = input("Ingrese la segunda fecha (dd/mm/aaaa): ")


# Se convierten los textos ingresados en fechas
fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")


# Se calcula la diferencia entre las dos fechas
diferencia = abs(fecha1 - fecha2)


# Se muestra la cantidad de días de diferencia
print("La diferencia entre las fechas es de", diferencia.days, "días")