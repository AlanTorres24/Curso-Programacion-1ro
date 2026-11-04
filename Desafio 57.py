# Clase principal Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    # Método para mostrar los datos del autor
    def mostrar_autor(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)


# Clase Poeta que hereda de Autor
class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Se inicializan los atributos heredados usando super()
        super().__init__(nombre, nacionalidad)

        # Se agrega el atributo propio de Poeta
        self.tipo_poesia = tipo_poesia

    # mostrar todos los datos del poeta
    def mostrar_poeta(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Tipo de poesía:", self.tipo_poesia)


# Creación de dos objetos Poeta
poeta1 = Poeta("Mario Benedetti", "Uruguayo", "Poesía amorosa")
poeta2 = Poeta("Pablo Neruda", "Chileno", "Poesía romántica")


# Se muestran los datos del primer poeta
print("Datos del primer poeta:")
poeta1.mostrar_poeta()

print()

# Se muestran los datos del segundo poeta
print("Datos del segundo poeta:")
poeta2.mostrar_poeta()


# Se comprueba el acceso a los atributos heredados
print()
print("Atributos heredados del primer poeta:")
print("Nombre:", poeta1.nombre)
print("Nacionalidad:", poeta1.nacionalidad)


# Se comprueba el uso de un método heredado de Autor
print()
print("Datos usando el método heredado de Autor:")
poeta1.mostrar_autor()