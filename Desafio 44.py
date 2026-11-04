# Lista que contiene los libros de la biblioteca
libros = []


# Función para agregar un libro
def agregar_libro(libro):
    libros.append(libro)


# Función para eliminar un libro
def eliminar_libro(libro):
    if libro in libros:
        libros.remove(libro)


# Función para buscar un libro por título
def buscar_libro(titulo):
    if titulo in libros:
        return True
    return False


# Función para mostrar todos los libros
def mostrar_libros():
    for libro in libros:
        print(libro)


# Se agregan cuatro libros
agregar_libro("El Principito")
agregar_libro("Harry Potter")
agregar_libro("Martín Fierro")
agregar_libro("programación en Python")


# Se muestran los libros disponibles
print("Libros disponibles:")
mostrar_libros()


# Se realiza una búsqueda
print("¿Está disponible El Principito?", buscar_libro("El Principito"))


# Se elimina un libro
eliminar_libro("Harry Potter")


# Se muestran nuevamente los libros
print("Libros después de eliminar Harry Potter:")
mostrar_libros()