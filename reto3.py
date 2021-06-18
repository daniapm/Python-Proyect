#!/usr/bin/python3
from colorama import init, Fore, Style
"""programa que permita realizar el proceso de ingreso de productos a un inventario de la 
   empresa Cloudata SAS."""
#creacion de variables
n_productos = []
codigo = []
tipo_producto = []
tipo_flete = []
cantidad_producto = []
costo_sin_iva = []
n_productos = 1
nombre = []
valor_flete = 0
porcentage_Ganacia = 0
opcion = 0
porcentaje_flete = 0
precio_Venta_PorProducto = 0
costo_Final_PorProducto = 0
ganancia_PorProducto = 0
total_de_los_productos = 0
ganacias_de_los_productos = 0
fletes_productos = 0
valor_total_venta = 0
costo_sin_flete = 0
total_costo_sin_flete = 0
#ciclo for para pedir por pantalla los 5 productos
for i in range(1, 6):
    print(Fore.MAGENTA + "Producto", i) #agregando color
    print(Style.RESET_ALL, end = "")
    #Pidiendo datos por teclado
    while True:
        try:
            nombre.append(str(input(f"Por favor ingresa el nombre del producto {i}: ")))
            break
        except TypeError:
            print(Fore.MAGENTA + ":( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
            print(Fore.MAGENTA + "Opp! debe ingresar un dato de tipo cadena")
            print(Fore.MAGENTA + ":( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
            print(Style.RESET_ALL, end = "")
    while True:
        try:
            codigo.append(int(input(f"Por favor ingresa el codigo del producto {i}: ")))
            tipo_producto.append(int(input(f"Por favor ingresa el tipo de producto. 1(fisico) o 2(servicio) {i}: ")))
            tipo_flete.append(int(input(f"Por favor ingresa el tipo de flete. 1(nacional) o 2(internacional) {i}: ")))
            cantidad_producto.append(int(input(f"Por favor ingresa la cantidad producto {i}: ")))
            costo_sin_iva.append(float(input(f"Por favor ingresa el costo sin iva del producto {i}: ")))
            break
        except (TypeError, ValueError):
            print(Fore.MAGENTA + ":( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
            print(Fore.RED + "Opp! debe ingresar un dato numerico")
            print(Fore.MAGENTA + ":( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
            print(Style.RESET_ALL, end = "")
    #condicionales para definir porcentaje de ganancia dependiendo el tipo de flete
    for tipo in tipo_producto:
        if (tipo == 2):
            porcentage_Ganacia = 0.35
        elif (tipo == 1):
            porcentage_Ganacia = 0.2
    #condicionales para definir valor de flete dependiendo el tipo de flete
    for tipo_f in tipo_flete:
        for costo in costo_sin_iva:
            if (tipo_f == 1):
                valor_flete = costo * 0.2
            elif (tipo_f == 2):
                valor_flete = costo * 0.45
                print(valor_flete)
            costo_Final_PorProducto = (float(costo) * 1.19) + float(valor_flete)
            print(valor_flete)
            ganancia_PorProducto = costo * porcentage_Ganacia
            costo_sin_flete = (float(costo) * 1.19)
        for cantidad in cantidad_producto:
            costo_Total_Producto = float(costo_Final_PorProducto) * float(cantidad)
            precio_Venta_PorProducto = (costo_Final_PorProducto) + (ganancia_PorProducto)

    #Imprimimos los resultadosnpor producto
    print("=================================================================")
    print(Fore.CYAN + f'Costo final por producto: {round(costo_Final_PorProducto, 2)}')
    print(f"precio Venta Producto: {round(precio_Venta_PorProducto, 2)}")
    print(f"costo Total Producto: {round(costo_Total_Producto, 2)}")
    print(f"ganancia Por Producto: {round(ganancia_PorProducto, 2)}")
    print(Style.RESET_ALL, end="")
    print("=================================================================")
    #calculamos totales de los productos ingresados
    total_de_los_productos += costo_Final_PorProducto
    ganacias_de_los_productos += ganancia_PorProducto
    fletes_productos += valor_flete
    valor_total_venta += precio_Venta_PorProducto
    total_costo_sin_flete += costo_sin_flete
    #imprimimos los totales de los productos ingresados
print("Por favor elija una de las siguientes opciones del menu: ")
opcion = input(" 1. Mostrar el costo total de los productos.\n\
 2. Mostrar el total de ganancia de los productos\n\
 3. Mostrar el total de fletes de los productos.\n\
 4. Mostrar el valor total de venta de los productos.\n\
 5. Mostrar el costo total de los productos sin incluir fletes.\n\
Escriba aqui su opcion: ")

#Menu de opciones para el usuario
#if (opcion == "1"):
print(Fore.BLUE + f"Opción 1: Total costo productos:", total_de_los_productos)
#elif (opcion == "2"):
print(Fore.BLUE + f"Opción 2: Total ganancia productos:", ganacias_de_los_productos)
#elif (opcion == "3"):
print(Fore.BLUE + f"Opción 3: Total flete productos:", fletes_productos)
#elif (opcion == "4"):
print(Fore.BLUE + f"Opción 4: Total valor venta productos:", valor_total_venta)
#elif (opcion == "5"):
print(Fore.BLUE + f"Opción 5: Total costo productos sin incluir fletes:", total_costo_sin_flete)
