#diferentes formas de recorrer un diccionario
diccionario = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
for llave in diccionario:
    print(llave)
for valor in diccionario.values():
    print(valor)
for llave, valor in diccionario.items():
    print("llave", llave, "valor", valor)

for clave in diccionario.keys():
    print("Producto:", clave)

keys(): #Devuelve sólo las claves.
values(): #Devuelve sólo los valores.
items(): #Devuelve los pares clave-valor.
clear(): #Elimina todos los elementos.
copy(): #Crea una copia del diccionario.
get(key, default): #Devuelve el valor asociado a la clave. Si no existe, devuelve default.
pop(key, default): #Elimina y devuelve el valor asociado a la clave. Si no existe, devuelve default.
setdefault(key, default): #Si la clave no existe, agrega la clave con valor default.
update(other_dict): #Actualiza el diccionario con los pares clave-valor de otro diccionario.
fromkeys(keys, default): #Crea un nuevo diccionario con las claves de la lista keys y valores default.
popitem(): #Elimina y devuelve un par clave-valor arbitrario.

