# Función recursiva para invertir las palabras de la oración
def invertir_palabras(palabras):
    if len(palabras) == 0:
        return ""
    
    return palabras[-1] + " " + invertir_palabras(palabras[:-1])


# Se le pide al usuario que ingrese una oración
oracion = input("Ingrese una oración: ")


# Se separa la oración en palabras
palabras = oracion.split()


# Se invierten las palabras de la oración
resultado = invertir_palabras(palabras)


# Se muestra el resultado
print("La oración invertida es:", resultado)