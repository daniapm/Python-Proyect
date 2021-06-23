# DICCIONARIOS

# DEFINIR UN DICCIONARIO VACIO
vacio = {}
print(vacio)
print("-------------------------------------------------------")

# DEFINICIÓN
colores = {'amarillo':'yellow', 'azul':'blue', 'rojo':'red'}
print(colores)

print("-------------------------------------------------------")
# imprimir el valor del primer elemento
print(colores['amarillo'])

print("-------------------------------------------------------")
# MUTABILIDAD EN LOS DICCIONARIOS
# agregar un elemento nuevo al diccionario
colores['verde'] = 'green'
print(colores)
# modificar un elemento usando la clave o llave
colores['verde'] = 'hola'
print(colores)
print("-------------------------------------------------------")

# BORRAR ELEMENTOS
del(colores['amarillo'])
print(colores)

print("-------------------------------------------------------")
numeros = {10:'diez', 20:'veinte'}
print(numeros[10])

# TRABAJAR DIRECTAMENTE CON SUS REGISTROS COMO SI FUERAN VARIABLES
print("-------------------------------------------------------")
edades = {'carlos':27, 'jhon':30, 'maria':50}
edades['carlos']+=1
print(edades)
print("-------------------------------------------------------")
print(edades['jhon'] + edades['maria'])

print("-------------------------------------------------------")
# EJECUTAR LECTURA SECUENCIAL FOR
for edad in edades:
    print(edad)

print("-------------------------------------------------------")
for clave in edades:
    print(clave, edades[clave])

print("-------------------------------------------------------")
# items() nos facilita la lectura en clave y valor de los elementos.
for clave, valor in edades.items():
    print(clave, valor)