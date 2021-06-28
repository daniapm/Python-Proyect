# LECTURA DE DATOS EN JSON DICCIONARIOS

import json

with open('contactos2.json', encoding='utf8') as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos["contactos"]:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])