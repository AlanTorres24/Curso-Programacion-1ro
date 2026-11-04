class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    # para agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # para eliminar un libro
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

    # para mostrar los datos del autor
    def mostrar_autor(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)


class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor


# creamos los autores
autor1 = Autor("Antoine de Saint-Exupéry", "Francés")
autor2 = Autor("José Hernández", "Argentino")
autor3 = Autor("J. K. Rowling", "Británica")
autor4 = Autor("Alan Torres", "Uruguayo")

# creamos los libros y los relacionamos con sus autores
libro1 = Libro("El Principito", "Fantasía", "001", autor1)
libro2 = Libro("Martin Fierro", "Poesía", "002", autor2)
libro3 = Libro("Harry Potter", "Fantasía", "003", autor3)
libro4 = Libro("Mis primeros pasos con Python", "Programación", "004", autor4)

# agregamos los libros a cada autor
autor1.agregar_libro(libro1.titulo)
autor2.agregar_libro(libro2.titulo)
autor3.agregar_libro(libro3.titulo)
autor4.agregar_libro(libro4.titulo)

# mostramos la información de los libros
print("Libro:", libro1.titulo)
print("Género:", libro1.genero)
print("ISBN:", libro1.isbn)
print("Autor:", libro1.autor.nombre)

print()

print("Libro:", libro2.titulo)
print("Género:", libro2.genero)
print("ISBN:", libro2.isbn)
print("Autor:", libro2.autor.nombre)

print()

print("Libro:", libro3.titulo)
print("Género:", libro3.genero)
print("ISBN:", libro3.isbn)
print("Autor:", libro3.autor.nombre)

print()

print("Libro:", libro4.titulo)
print("Género:", libro4.genero)
print("ISBN:", libro4.isbn)
print("Autor:", libro4.autor.nombre)