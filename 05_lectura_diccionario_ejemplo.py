# LEER UN CSV ESCRITO EN FORMA DE DICCIONARIO

# importamos el modulo de csv para trabajar archivos de este tipo
import csv

with open("productos.csv", "r", newline="\n", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for producto in reader:
        print(producto["nombre"], producto["codigo"], producto["tipoproducto"], producto["tipoflete"], producto["cantidad"], producto["precio"])