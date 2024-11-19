"""Gestión de descuentos

Optativos | No entregables

Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. Vas a desarrollar un programa que permita
calcular el precio final de un producto después de aplicar un descuento. Para hacerlo:

Crea una función que reciba como parámetros el precio original del producto y el porcentaje de descuento, y que retorne
el precio final con el descuento aplicado.

Luego, pedí que se ingrese el precio y el porcentaje de descuento. Mostrá el precio final después de aplicar el descuento."""
def descuento(precio, porcentaje):
    precio_final = precio - (precio * porcentaje / 100)
    return precio_final
try:
    precio = float(input("Ingrese el precio del producto: "))
    porcentaje = float(input("Ingrese el porcentaje de descuento: "))
except ValueError:
    print("Debe ingresar un numero")

precio_final = descuento(precio, porcentaje)
print("El precio final con descuento es: ", precio_final)   


################################################################

