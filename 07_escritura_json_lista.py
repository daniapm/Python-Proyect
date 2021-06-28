# ESCRITURA DE DATOS EN JSON UTILIZANDO LISTAS

# importar el modulo json
import json

contactos = [
    ("manuel", "desarrollador web", "manuel@ejemplo.com"),
    ("lorena", "gerente de proyectos", "lorena@ejemplo.com"),
    ("javier", "analista de datos", "javier@ejemplo.com"),
    ("martha", "experta en python", "martha@ejemplo.com")
]

datos = []

for nombre, empleo, email in contactos:
    datos.append({"nombre": nombre, "empleo": empleo, "email": email})

with open('contactos.json', 'w', encoding='utf8') as jsonfile:
    json.dump(datos, jsonfile)


