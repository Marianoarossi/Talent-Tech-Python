"""Consultar stock en inventario

Optativos | No entregables

El inventario de una tienda está almacenado en un diccionario, donde las claves son los nombres de los
productos y los valores son las cantidades disponibles en stock. Creá un programa que:

Te permita ingresar el nombre de un producto.

Utilice el método .get() para buscar el stock disponible. Si el producto no existe, deberá mostrar un
mensaje diciendo "Producto no encontrado".

Si el producto está disponible, mostrará cuántas unidades quedan en stock.

Ejercicios prácticos

Consultar stock en inventario

Optativos | No entregables

productos = {

"Manzanas": 50,

"Naranjas": 30,

"Peras": 25

}

Diccionario inicial:

Ingresá el nombre del producto: Peras

Stock disponible de Peras: 25"""
productos = {

"Manzanas": 50,

"Naranjas": 30,

"Peras": 25

}
mensaje= "Producto no encontrado"
while True:
    producto = input("Ingrese el nombre del producto o 'salir' para finalizar: ").lower()
    if producto == "salir":
        break
    else:
        dato= productos.get(producto, mensaje)
        if dato == mensaje:
            print(mensaje)
        else:
            print(dato)