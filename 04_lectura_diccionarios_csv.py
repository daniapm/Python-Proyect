# LECTURA DE DICCIONARIOS EN CSV

# importamos el modulo de csv para poder trabajar con los archivos
import csv

# DictReader es un lector para leer cada fila de un archivo csv escrito en forma de diccionario
with open("contactos2.csv", "r", newline="\n", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    # recorremos cada contacto del archivo csv
    for contacto in reader:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])