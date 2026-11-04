#Desafío 3: Suma de los primeros n números enteros
def suma_numeros_enteros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
# Ejemplo de uso
print("Suma de los primeros n números enteros")
n = 10
resultado = suma_numeros_enteros(n)
print(f"La suma de los primeros {n} números enteros es: {resultado}")



# Desafío 4: Número de elementos pares en una lista
def contar_pares(lista):
    contador_pares = 0
    for num in lista:
        if num % 2 == 0:
            contador_pares += 1
    return contador_pares

# Ejemplo de uso
print(" Número de elementos pares en una lista ")
Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = contar_pares(Lista)
print(f"Lista: {Lista}")
print(f"Cantidad de números pares: {resultado}")