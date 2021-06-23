# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar 
# los precios de las distintas frutas. El programa pedirá el nombre de la fruta 
# y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir 
# de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

precios = {'manzana':1000, 'naranja': 500, 'platano': 600, 'pera':1500}

while(True):
    fruta = input("Ingrese el nombre la fruta que vas a vender: ")

    if fruta.lower() not in precios:
        print("Fruta no existe")
    else:
        cantidad = int(input("Ingrese la cantidad a vender de la fruta: "))
        precioTotal = cantidad * precios[fruta]
        print(f"El precio de la venta es: {precioTotal}")
    
    opcion = input("¿Quiere vender otra fruta (s/n)?")

    while opcion.lower() != 's' and opcion.lower() != 'n':
        opcion = input("¿Quiere vender otra fruta (s/n)?")
    if opcion.lower() == 'n':
        break

