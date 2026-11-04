# Lista de estudiantes ordenada alfabéticamente
estudiantes = ["Ana", "Bruno", "Carlos", "Diego", "Lucía", "María", "Pedro"]

# Función para buscar un estudiante
def busqueda_binaria(estudiantes, nombre_buscar):
    bajo = 0
    alto = len(estudiantes) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2

        if estudiantes[medio] == nombre_buscar:
            return medio
        elif estudiantes[medio] < nombre_buscar:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1


# Se solicita el nombre del estudiante
nombre = input("Ingrese el nombre del estudiante que desea buscar: ")

# Se realiza la búsqueda
resultado = busqueda_binaria(estudiantes, nombre)

# Se muestra el resultado
if resultado != -1:
    print("El estudiante", nombre, "se encuentra en la posición", resultado)
else:
    print("El estudiante", nombre, "no se encuentra en la lista.")