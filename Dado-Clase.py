import random

def tirar_dado(limite_inferior, limite_superior, cantidad):
    azar = random.randint(limite_inferior, limite_superior)

def pedir_limites():
    while True:
        try:
            limite_inferior = int(input("Ingrese el límite inferior: "))
            limite_superior = int(input("Ingrese el límite superior: "))
            return limite_inferior, limite_superior
        except ValueError:
            print("Error: debe ingresar números enteros. Intente nuevamente.")