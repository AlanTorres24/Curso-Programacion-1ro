# Clase base Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


# Clase LibroDigital que hereda de Libro
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    # Muestra la información del libro digital
    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)
        print("Formato:", self.formato)
        print("Tamaño del archivo:", self.tamaño_archivo)


# Clase EBook que hereda de LibroDigital
class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    # Se sobrescribe el método para agregar el enlace
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Enlace de descarga:", self.enlace_descarga)


# Se crean los objetos
libro_digital = LibroDigital(
    "El Principito",
    "Antoine de Saint-Exupéry",
    "978-0156012195",
    "PDF",
    "2 MB"
)

ebook = EBook(
    "Harry Potter",
    "J. K. Rowling",
    "978-8478884459",
    "EPUB",
    "4 MB",
    "www.ebook.com/harry-potter"
)


# Se muestra la información de ambos objetos
print("Información del Libro Digital:")
libro_digital.mostrar_informacion()

print("\nInformación del EBook:")
ebook.mostrar_informacion()