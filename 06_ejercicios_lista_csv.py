# Calcular el promedio de precios y el promedio de la calificación de un lista de juegos que 
# debe ser leído desde un archivo llamado videojuegos.csv

import csv 

with open("videojuegos.csv", "r", newline="\n", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    # omitir el encabezado
    next(reader, None)

    acumuladorCalificacion = 0
    acumuladorPrecios = 0
    contador = 0

    for videojuego in reader:
        nombreJuego = videojuego[0]
        calificacionJuego = int(videojuego[1])
        precioJuego = float(videojuego[2])

        acumuladorCalificacion = acumuladorCalificacion + calificacionJuego
        acumuladorPrecios = acumuladorPrecios + precioJuego
        contador = contador + 1

    promedioCalificacion = acumuladorCalificacion / contador
    promedioPrecios = acumuladorPrecios / contador
    print(f"El promedio de precios es: {promedioPrecios} y el promedio de calificación es: {round(promedioCalificacion, 2)}")