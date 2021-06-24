#!/usr/bin/python3
"""programa que permita realizar el proceso de ingreso de productos a un inventario de la 
   empresa Cloudata SAS."""
#creacion de variables
n_productos = 0
codigo = 0
tipo_producto = 0
tipo_flete = 0
cantidad_producto = 0
costo_sin_iva = 0
n_productos = 1
nombre = 0
lista_inventario = []
producto1 = {}
producto2 = {}
producto3 = {}
producto4 = {}
producto5 = {}
valor_flete = 0
porcentage_Ganacia = 0
opcion = 0
porcentaje_flete = 0
precio_Venta_PorProducto = 0
costo_Final_PorProducto = 0
ganancia_PorProducto = 0
costo_Total_Producto = 0
total_de_los_productos = 0
ganacias_de_los_productos = 0
fletes_productos = 0
valor_total_venta = 0
costo_sin_flete = 0
total_costo_sin_flete = 0

def calculando_productos(tipo_producto, tipo_flete, cantidad_producto, costo_sin_iva):
    if tipo_flete == 1:
        valor_flete = costo_sin_iva* 20 / 100
    elif tipo_flete == 2:
        valor_flete = costo_sin_iva * 45 / 100
    costo_Total_Producto = (costo_sin_iva * 1.19) + valor_flete
    if tipo_producto == 1:
        ganancia_PorProducto = costo_sin_iva * 20 / 100
    elif tipo_producto == 2:
        ganancia_PorProducto = costo_sin_iva * 35 / 100
    costo_Final_PorProducto = costo_sin_iva * 1.19 + valor_flete
    precio_Venta_PorProducto = costo_Final_PorProducto + ganancia_PorProducto
    costo_sin_flete = costo_sin_iva * 1.19
    costo_Total_Producto = costo_Final_PorProducto * cantidad_producto
    return valor_flete, costo_Final_PorProducto, ganancia_PorProducto, precio_Venta_PorProducto, costo_sin_flete, costo_Total_Producto

#ciclo for para pedir por pantalla los 5 productos
for i in range(1, 6):
    print("PRODUCTO", i)
    #Pidiendo datos por teclado
    nombre = (str(input(f"Por favor ingresa el nombre del producto {i}: ")))
    while True:
        try:
            codigo = (int(input(f"Por favor ingresa el codigo del producto {i}: ")))
            break
        except (TypeError, ValueError):
            print("-----------------------------------------------")
            print("Opp! el codigo debe ser un dato de tipo numerico")
            print("-----------------------------------------------")
    while True:
        try:
            tipo_producto = (int(input(f"Por favor ingresa el tipo de producto. 1(fisico) o 2(servicio) del producto {i}: ")))
            if tipo_producto == 1 or tipo_producto == 2:
                break
            else:
                print("Opp! debes ingresar la opcion 1 o 2")
        except (TypeError, ValueError):
            print("-------------------------------------------------------")
            print("Opp! el tipo de producto debe ser un dato de tipo numerico")
            print("-------------------------------------------------------")
    while True:
        try:
            tipo_flete = (int(input(f"Por favor ingresa el tipo de flete. 1(nacional) o 2(internacional) del producto {i}: ")))
            if tipo_flete == 1 or tipo_flete == 2:
                break
            else:
                print("Opp! debes ingresar la opcion 1 o 2")
        except (TypeError, ValueError):
            print("-----------------------------------------------")
            print("Opp! el tipo de flete debe ser un dato numerico")
            print("-----------------------------------------------")
    while True:
        try:
            cantidad_producto = (int(input(f"Por favor ingresa la cantidad producto {i}: ")))
            break
        except (TypeError, ValueError):
            print("-----------------------------------------------")
            print("Opp! la cantidad del producto debe ser un dato numerico")
            print("-----------------------------------------------")
    while True:
        try:
            costo_sin_iva = (float(input(f"Por favor ingresa el costo sin iva del producto {i}: ")))
            break
        except (TypeError, ValueError):
            print("-----------------------------------------------")
            print("Opp! el costo sin iva debe ser un dato numerico")
            print("-----------------------------------------------")
    if i == 1:
        producto1 = {"nombre": nombre, "codigo": codigo, "tipo_producto": tipo_producto, "tipo_flete": tipo_flete, "cantidad_producto": cantidad_producto, "costo_sin_iva": costo_sin_iva}
        lista_inventario.append(producto1)
    elif i == 2:
        producto2 = {"nombre": nombre, "codigo": codigo, "tipo_producto": tipo_producto, "tipo_flete": tipo_flete, "cantidad_producto": cantidad_producto, "costo_sin_iva": costo_sin_iva}
        lista_inventario.append(producto2)
    elif i == 3:
        producto3 = {"nombre": nombre, "codigo": codigo, "tipo_producto": tipo_producto, "tipo_flete": tipo_flete, "cantidad_producto": cantidad_producto, "costo_sin_iva": costo_sin_iva}
        lista_inventario.append(producto3)
    elif i == 4:
        producto4 = {"nombre": nombre, "codigo": codigo, "tipo_producto": tipo_producto, "tipo_flete": tipo_flete, "cantidad_producto": cantidad_producto, "costo_sin_iva": costo_sin_iva}
        lista_inventario.append(producto4)
    elif i == 5:
        producto5 = {"nombre": nombre, "codigo": codigo, "tipo_producto": tipo_producto, "tipo_flete": tipo_flete, "cantidad_producto": cantidad_producto, "costo_sin_iva": costo_sin_iva}
        lista_inventario.append(producto5)

lista_result_inventario = []
for producto in lista_inventario:
    lista_result_inventario.append(calculando_productos(producto["tipo_producto"], producto["tipo_flete"], producto["cantidad_producto"], producto["costo_sin_iva"]))
contador = 1
for position in lista_result_inventario:
    costo_Final_PorProducto = round(position[1],2)
    precio_Venta_PorProducto = round(position[3],2)
    costo_Total_Producto = round(position[5],2)
    ganancia_PorProducto = round(position[2],2)
    costo_sin_flete = round(position[4],2)
    valor_flete = round(position[0],2)
    print(f"RESUMEN PRODUCTO {contador} ========================")
    print(f'Costo final por producto: {round(costo_Final_PorProducto, 2)}')
    print(f"precio Venta Producto: {round(precio_Venta_PorProducto, 2)}")
    print(f"costo Total Producto: {round(costo_Total_Producto, 2)}")
    print(f"ganancia Por Producto: {round(ganancia_PorProducto, 2)}")
    print("=======================================================")
    contador += 1

    #calculamos totales de los productos ingresados
    total_de_los_productos += costo_Final_PorProducto
    ganacias_de_los_productos += ganancia_PorProducto
    fletes_productos += valor_flete
    valor_total_venta += precio_Venta_PorProducto
    total_costo_sin_flete += costo_sin_flete

while (True):
    try:
        opcion = int(input(" \n 1.    Mostrar el costo total de los productos \n 2.    Mostrar el total de ganancia de los productos \n 3.    Mostrar el total de fletes de los productos \n 4.    Mostrar el valor total de venta de los productos \n 5.    Mostrar el costo total de los productos sin incluir fletes \n 0.    Salir del menu\n" ))
        if (opcion == 1):
            print(f"Opción 1: Total costo productos:", total_de_los_productos)
        elif (opcion == 2):
            print(f"Opción 2: Total ganancia productos:", ganacias_de_los_productos)
        elif (opcion == 3):
            print(f"Opción 3: Total flete productos:", fletes_productos)
        elif (opcion == 4):
            print(f"Opción 4: Total valor venta productos:", valor_total_venta)
        elif (opcion == 5):
            print(f"Opción 5: Total costo productos sin incluir fletes:", total_costo_sin_flete)
        if opcion == 0:
            break
    except:
        print("El valor ingresado no esta en el menu")
