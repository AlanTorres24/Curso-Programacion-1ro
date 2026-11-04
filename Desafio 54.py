# Se crea la clase Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    # Getter para obtener el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Setter para modificar el nombre
    @nombre.setter
    def nombre(self, nombre):
        if nombre != "":
            self.__nombre = nombre
        else:
            print("El nombre no puede estar vacío")

    # obtener la nacionalidad
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Setter para modificar la nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        if nacionalidad != "":
            self.__nacionalidad = nacionalidad
        else:
            print("La nacionalidad no puede estar vacía")


# Se crea un objeto de la clase Autor
autor = Autor("Mario Benedetti", "Uruguayo")


# Se muestran los datos del autor
print("Nombre:", autor.nombre)
print("Nacionalidad:", autor.nacionalidad)


# Se modifican los datos mediante los setter
autor.nombre = "Stephen King"
autor.nacionalidad = "Estadounidense"


# Se muestran los datos modificados
print("Nombre modificado:", autor.nombre)
print("Nacionalidad modificada:", autor.nacionalidad)


# Se intenta asignar un valor vacío
autor.nombre = ""
autor.nacionalidad = ""