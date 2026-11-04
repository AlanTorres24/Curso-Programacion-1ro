# Función que verifica si un número es primo
def es_primo(numero):
    """
    Recibe un numero y devuelve True si es primo.
    Devuelve False en caso contrario.
    """

    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


# Función que cuenta cuantos numeros primos hay en una lista
def contar_primos(lista):
    """
    Recibe una lista de numeros y devuelve
    la cantidad de numeros primos.
    """

    cantidad = 0

    for numero in lista:
        if es_primo(numero):
            cantidad += 1

    return cantidad


# Programa principal
def main():
    numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    print("Lista:", numeros)

    cantidad = contar_primos(numeros)

    print("Cantidad de números primos:", cantidad)


main()