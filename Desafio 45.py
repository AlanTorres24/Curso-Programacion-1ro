# Creamos dos bibliotecas
biblioteca1 = []
biblioteca2 = []


# Función para agregar un libro
def agregar(biblioteca, libro):
    biblioteca.append(libro)


# Función para eliminar un libro
def eliminar(biblioteca, libro):
    if libro in biblioteca:
        biblioteca.remove(libro)


# Función para buscar un libro
def buscar(biblioteca, libro):
    return libro in biblioteca


# Función para mostrar los libros
def mostrar(biblioteca):
    for libro in biblioteca:
        print(libro)


# Agregamos libros a la primera biblioteca
agregar(biblioteca1, "El Principito")
agregar(biblioteca1, "Martin Fierro")

# Agregamos libros a la segunda biblioteca
agregar(biblioteca2, "Harry Potter")
agregar(biblioteca2, "Programacion en Python")


# Mostramos la primera biblioteca
print("Biblioteca 1:")
mostrar(biblioteca1)

# Mostramos la segunda biblioteca
print("Biblioteca 2:")
mostrar(biblioteca2)


# Buscamos un libro
print("¿Está El Principito en la biblioteca 1?", buscar(biblioteca1, "El Principito"))


# Eliminamos un libro
eliminar(biblioteca2, "Harry Potter")


# Mostramos nuevamente la biblioteca 2
print("Biblioteca 2 después de eliminar:")
mostrar(biblioteca2)