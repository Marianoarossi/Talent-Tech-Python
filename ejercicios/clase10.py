"""En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa que permita:

Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un diccionario donde
la clave es el nombre del producto y el valor es su precio.

Una vez ingresados, mostrará todos los productos y sus precios en pantalla.

Ejemplo de salida esperada.

Producto: Manzanas, Precio: 100

Producto: Naranjas, Precio: 150

Producto: Peras, Precio: 120"""
productos={}
for i in range(3):
    producto=input("ingrese el nombre del producto: ").lower()
    precio= float(input("ingrese el precio del producto: "))
    productos[producto]=precio

    for producto, precio in productos.items():
        print("Producto:", producto, "Precio:", precio)


#Se utiliza para convertir el primer letra en mayusculas .capitalize()
