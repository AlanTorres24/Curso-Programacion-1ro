class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    # Método para agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para eliminar un libro
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)


# Creamos los autores
autor1 = Autor("Antoine de Saint-Exupéry", "Francés")
autor2 = Autor("José Hernández", "Argentino")
autor3 = Autor("J. K. Rowling", "Británica")
autor4 = Autor("Alan Torres", "Uruguayo")

# Agregamos los libros
autor1.agregar_libro("El Principito")
autor2.agregar_libro("Martin Fierro")
autor3.agregar_libro("Harry Potter")
autor4.agregar_libro("Programacion en Python")

# Mostramos los libros de cada autor
print("Libros de Antoine de Saint-Exupéry:")
for libro in autor1.libros:
    print(libro)

print("Libros de José Hernández:")
for libro in autor2.libros:
    print(libro)

print("Libros de J. K. Rowling:")
for libro in autor3.libros:
    print(libro)

print("Libros de Alan Torres:")
for libro in autor4.libros:
    print(libro)

# Eliminamos un libro
autor3.eliminar_libro("Harry Potter")

# Mostramos nuevamente los libros de J. K. Rowling
print("Libros de J. K. Rowling después de eliminar Harry Potter: ")
for libro in autor3.libros:
    print(libro) 
else:
    print("No hay libros disponibles del autor.")
    