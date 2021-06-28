# LECTURA DE DATOS EN JSON LISTAS

import json

with open('contactos.json', encoding='utf8') as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])