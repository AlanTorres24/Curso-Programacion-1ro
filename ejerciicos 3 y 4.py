def contar_pares(lista):
    contador_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            contador_pares = contador_pares + 1
    return contador_pares

# Ejemplo de uso
print("Número de elementos pares en una lista")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = contar_pares(lista)
print(f"Lista: {lista}")
print(f"Cantidad de números pares: {resultado}")