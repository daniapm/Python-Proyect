# Escribe un programa que lea una cadena 
# y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena. 

diccionarioCadena = {}

cadena = input("Ingrese una cadena: ")

for caracter in cadena:
    if caracter in diccionarioCadena:
        diccionarioCadena[caracter]+=1
    else:
        diccionarioCadena[caracter]=1

for clave, valor in diccionarioCadena.items():
    print(f"{clave} => {valor}")