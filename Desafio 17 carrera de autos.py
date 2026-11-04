import random
# Nombres de los autos
autos = ["Auto 1", "Auto 2", "Auto 3", "Auto 4"]

# Distancia recorrida por auto
distancias = [0, 0, 0, 0]

# La carrera dura 10 segundos
for segundo in range(10):

    print("Segundo", segundo + 1)

    
    # Cada auto avanza una distancia según una velocidad aleatoria
    for i in range(len(autos)):

        velocidad = random.randint(10, 20)

        distancias[i] = distancias[i] + velocidad

        print(autos[i], "avanzó", velocidad, "metros. Distancia total:", distancias[i])


    print()


# Se busca la mayor distancia recorrida
mayor_distancia = max(distancias)


# Lista para guardar a los ganadores
ganadores = []


# Verifica qué autos llegaron a la mayor distancia
for i in range(len(autos)):

    if distancias[i] == mayor_distancia:

        ganadores.append(autos[i])


# Muestra el resultado final
if len(ganadores) == 1:

    print("El ganador de la carrera es el", ganadores[0])

else:

    print("Hubo un empate entre:", ganadores)