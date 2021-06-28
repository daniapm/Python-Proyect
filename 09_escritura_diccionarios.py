# ESCRITURA DE DATOS EN JSON UTILIZANDO DICCIONARIOS

# importar el modulo json
import json

contactos = [
    ("manuel", "desarrollador web", "manuel@ejemplo.com"),
    ("lorena", "gerente de proyectos", "lorena@ejemplo.com"),
    ("javier", "analista de datos", "javier@ejemplo.com"),
    ("martha", "experta en python", "martha@ejemplo.com")
]

datos = {"contactos": []}

for nombre, empleo, email in contactos:
    datos["contactos"].append({"nombre": nombre, "empleo": empleo, "email": email})

with open('contactos2.json', 'w', encoding='utf8') as jsonfile:
    json.dump(datos, jsonfile)