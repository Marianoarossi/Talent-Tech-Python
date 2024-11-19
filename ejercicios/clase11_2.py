""""Cálculo de promedio de ventas

Optativos | No entregables

Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

Creá una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas ventas.

Con una función Solicitá a la persona que ingrese las ventas de cada día durante los días que elija el usaurio. Usá la función para calcular y
mostrar el promedio de ventas al finalizar."""

def calculo_promedio(ventas= []):
    promedio=0
    ventas_totales = 0
    for venta in ventas:
        ventas_totales += venta
    cantidad_dias = len(ventas)
    promedio = ventas_totales / cantidad_dias
    return promedio

def solicitar_ventas(dias):
    ventas =[]
    for dia in range(dias):
        venta = float(input(f"Ingrese las ventas del dia {dia+1}: "))
        ventas.append(venta)
    return ventas

while True:
    try:
        dias = int(input("Ingrese la cantidad de dias: "))
        if dias <= 0:
            print("Debe ingresar un numero mayor a 0")
        else:
            ventas=(solicitar_ventas(dias))
            promedio=calculo_promedio(ventas)
            print(f"El promedio de {dias} dias de ventas es: {promedio:.2f}")
    except ValueError:
        print("Debe ingresar un numero")


    

