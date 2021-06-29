"""programa que lea los productos del inventario de la empresa Cloudata SAS. a partir de unn archivo csv"""

import csv
import json
from os import write

#Funcion que hace el calculos de los productos:
def calculando_productos(tipo_producto, tipo_flete, cantidad_producto, costo_sin_iva):
    if tipo_flete == "1":
        valor_flete = int(costo_sin_iva) * 20 / 100
    elif tipo_flete == "2":
        valor_flete = int(costo_sin_iva) * 45 / 100
    costo_Total_Producto = (float(costo_sin_iva) * 1.19) + float(valor_flete)
    if tipo_producto == "1":
        ganancia_PorProducto = float(costo_sin_iva) * 20 / 100
    elif tipo_producto == "2":
        ganancia_PorProducto = float(costo_sin_iva) * 35 / 100
    costo_Final_PorProducto = float(costo_sin_iva) * 1.19 + float(valor_flete)
    precio_Venta_PorProducto = costo_Final_PorProducto + ganancia_PorProducto
    costo_sin_flete = (float(costo_sin_iva) * 1.19)
    costo_Total_Producto = float(costo_Final_PorProducto) * float(cantidad_producto)
    return valor_flete, costo_Final_PorProducto, ganancia_PorProducto, precio_Venta_PorProducto, costo_sin_flete, costo_Total_Producto

lista_result_inventario = []
#leemos el archivo productos.csv que contiene la informaciond de los productos:
with open("productos.csv", "r", newline="\n", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for productos in reader:
        #creamos la lista donde almacenaremos los resultados de las operaciones de cada produto:
        lista_result_inventario.append(calculando_productos(productos["tipo_producto"], productos["tipo_flete"], productos["cantidad_producto"], productos["costo_sin_iva"]))
    contador = 1
    total_de_los_productos = 0
    ganacias_de_los_productos = 0
    fletes_productos = 0
    valor_total_venta = 0
    total_costo_sin_flete = 0
    #recorremos la lista para hallar los resultados de los productos:
    for position in lista_result_inventario:
        costo_Final_PorProducto = round(position[1],2)
        precio_Venta_PorProducto = round(position[3],2)
        costo_Total_Producto = round(position[5],2)
        ganancia_PorProducto = round(position[2],2)
        costo_sin_flete = round(position[4],2)
        valor_flete = round(position[0],2)
        # imprimimos los resultados de cada producto (posteriormente estos resultados
        # se guardaran en un archivo .json por nombre producto)
        print(f"RESUMEN PRODUCTO {contador} ========================")
        print(f'Costo final por producto: {round(costo_Final_PorProducto, 2)}')
        print(f"precio Venta Producto: {round(precio_Venta_PorProducto, 2)}")
        print(f"costo Total Producto: {round(costo_Total_Producto, 2)}")
        print(f"ganancia Por Producto: {round(ganancia_PorProducto, 2)}")
        print("=======================================================")
        contador += 1
        #calculamos totales de los productos ingresados acumulandolos
        total_de_los_productos += costo_Final_PorProducto
        ganacias_de_los_productos+= ganancia_PorProducto
        fletes_productos += valor_flete
        valor_total_venta += precio_Venta_PorProducto
        total_costo_sin_flete += costo_sin_flete
        datos = []
        # Almacenamos los totales de cada producto en un archivo .json por cada producto
        datos.append({"costo final": costo_Final_PorProducto, "precio_venta": precio_Venta_PorProducto, "costo_total": costo_Total_Producto, "ganancia_producto": ganancia_PorProducto})
        with open(productos["nombre"]  +  ".json" , 'w', encoding='utf8') as jsonfile:
            json.dump(datos, jsonfile)
    # Menu para el usuario
    opcion = (int(input(f"Como desea ver la informacion de los productos?\n 1. Imprimir\n 2. Exportar los resultados a un archivo csv\n")))
    # Si el usuario desea mostrar por pantalla
    if opcion == 1:
        print(f"Total costo productos:", total_de_los_productos)
        print(f"Total ganancia productos:", ganacias_de_los_productos)
        print(f"Total flete productos:", fletes_productos)
        print(f"Total valor venta productos:", valor_total_venta)
        print(f"Total costo productos sin incluir fletes:", total_costo_sin_flete)
    # Si el usuario quiere almacenar en un archivo csv
    elif opcion == 2:
        totales = [(total_de_los_productos, ganacias_de_los_productos, fletes_productos, valor_total_venta, total_costo_sin_flete)]
        with open("totales.csv", "w", newline="\n", encoding='utf8') as csvfile:
            campos = ["total_costo_productos", "total_ganancia_productos", "total_flete_productos", "total_venta_productos", "total_costo_productos_sin_flete"]
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            for total_de_los_productos, ganacias_de_los_productos, fletes_productos, valor_total_venta, total_costo_sin_flete in totales:
                writer.writerow({"total_costo_productos": total_de_los_productos, "total_ganancia_productos": ganacias_de_los_productos, "total_flete_productos": fletes_productos, "total_venta_productos": valor_total_venta, "total_costo_productos_sin_flete": total_costo_sin_flete})
