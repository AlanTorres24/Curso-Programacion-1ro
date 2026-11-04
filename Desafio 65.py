# clase base para las figuras
class Figura:
    def area(self):
        pass


# clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    # Se calcula el área del círculo
    def area(self):
        return 3.14 * self.radio ** 2


# clase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    # Se calcula el área del cuadrado
    def area(self):
        return self.lado ** 2


# se crean los objetos
circulo = Circulo(5)
cuadrado = Cuadrado(4)

# se guardan los objetos en una misma lista
figuras = [circulo, cuadrado]

# recorre la lista y se calcula el área de cada figura
for figura in figuras:
    print("Figura:", figura.__class__.__name__)
    print("Área:", figura.area())