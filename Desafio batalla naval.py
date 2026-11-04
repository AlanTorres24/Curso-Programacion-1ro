import numpy as np
import random

# Se crea un tablero de 5x5 lleno de ceros
tablero = np.zeros((5, 5), dtype=int)

# Se colocan 3 barcos en posiciones aleatorias
for i in range(3):
    fila = random.randint(0, 4)
    columna = random.randint(0, 4)

    while tablero[fila][columna] == 1:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)

    tablero[fila][columna] = 1


# Función para verificar si hay un barco
def disparar(x, y):
    if tablero[x][y] == 1:
        print("Felicidades, le pegaste a un barco.")
    else:
        print("El disparo cayó al agua.")


# Se muestra el tablero
print(tablero)

# Ejemplo de disparo
disparar(2, 3)