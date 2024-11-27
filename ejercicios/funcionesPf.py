"""Necesitamos una función registrar_producto() que se encargue de agregar los productos en el diccionario
inventario con un código único y sus respectivos datos. La función pedirá que se ingrese los detalles del
producto y los almacenará en el diccionario.
Usaremos una variable que actúe como un contador para los códigos de los productos, así cada vez que se registra
un producto, se le asigna automáticamente un código nuevo.

El diccionario inventario usará el código del producto como clave, mientras que los valores asociados a esa clave
serán otro diccionario que contendrá toda la información del producto.

Podemos emplear un diccionario como estructura de datos para el inventario de productos. Usamos una clave
para cada dato que queremos almacenar. Por ejemplo:

Diccionario “inventario”:

inventario = {

1: {"nombre": "Manzana", "descripcion": "Fruta fresca",

"cantidad": 50, "precio": 0.5, "categoria": "Frutas"},

2: {"nombre": "Pan", "descripcion": "Pan casero",

"cantidad": 20, "precio": 1.0, "categoria": "Panadería"}

}
"""

inventario = {

1: {"nombre": "Manzana", "descripcion": "Fruta fresca",

"cantidad": 50, "precio": 0.5, "categoria": "Frutas"},

2: {"nombre": "Pan", "descripcion": "Pan casero",

"cantidad": 20, "precio": 1.0, "categoria": "Panadería"}

}

contador = 2

def registro_productos():
    codigo_producto = len(inventario) + 1  
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    descripcion = input("Ingrese la descripción del producto: ").capitalize()
    cantidad= 0
    precio=0.0
    while cantidad <=0:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad <=0:
                print("ingrese unnum mayor que 0")
            else:
                print("Error: La cantidad debe ser un número entero positivo o mayor que 0.") 

        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
            cantidad = 0




















def registrar_producto():
    global codigo
    codigo += 1
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")
    inventario[codigo] = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio, "categoria": categoria}
    print("Producto registrado con éxito.")

def mostrar_productos(inventario = inventario):
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
    else:
        
        for codigo, producto in inventario.items():
            print(f"Código: {codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoría: {producto['categoria']}")
            print()
            print("--------------------------------------------------")

def actualizar_stock():
    codigo = int(input("Ingrese el código del producto que desea actualizar: "))
    if codigo in inventario:
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        inventario[codigo]["cantidad"] = cantidad
        print("Stock actualizado con éxito.")

    else:
        print("El producto no existe en el inventario.")
        print("--------------------------------------------------")

def informe_productos():
    for codigo, producto in inventario.items():
        print(f"Código: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print(f"Categoría: {producto['categoria']}")



def reporte_bajo_stock():
    print("Productos con bajo stock (menos de 10 unidades):")
    for codigo, producto in inventario.items():
        if producto["cantidad"] < 10:
            print(f"Código: {codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print()

def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desea buscar: ").lower()
    encontrado = False
    for codigo, producto in inventario.items():
        if producto["nombre"].lower() == nombre:
            print(f"Código: {codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoría: {producto['categoria']}")
            encontrado = True
            break
    if not encontrado:
        print("El producto no existe en el inventario.")
        print("--------------------------------------------------")
        print("--------------------------------------------------")

def eliminar_producto():
    codigo = int(input("Ingrese el código del producto que desea eliminar: "))
    if codigo in inventario:
        del inventario[codigo]
        print("Producto eliminado con éxito.")

    else:
        print("El producto no existe en el inventario.")
        print("--------------------------------------------------")
        print("--------------------------------------------------")


"""En aplicaciones como la que estamos desarrollando, es necesario contar con una opción que permita actualizar
los datos almacenados. Para ello, escribiremos la función actualizar_producto().

Esta función debería solicitar que se ingrese el código del producto a actualizar, y verificar si existe en nuestro
diccionario. En caso afirmativo se piden el o los datos a actualizar y se efectúa el reemplazo de los valores en el
diccionario. Si el producto cuyo código hemos ingresado no existe, se puede mostrar un mensaje explicando la
situación antes de salir de la función.

Por supuesto, ¡puedes agregar todas las funcionalidades extra que consideres necesario!"""
def actualizar_producto():
    codigo = int(input("Ingrese el código del producto que desea actualizar: "))
    if codigo in inventario:
        nombre = input("Ingrese el nuevo nombre del producto: ")
        descripcion = input("Ingrese la nueva descripción del producto: ")
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        precio = float(input("Ingrese el nuevo precio del producto: "))
        categoria = input("Ingrese la nueva categoría del producto: ")
        inventario[codigo] = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio, "categoria": categoria}
        print("Producto actualizado con éxito.")
    else:
        print("El producto no existe en el inventario.")
        print("--------------------------------------------------")
        print("--------------------------------------------------")

def listar_Stock_bajo(inventario):
    print("Productos con bajo stock (menos de 10 unidades):")
    for codigo, producto in inventario.items():
        if producto["cantidad"] < 10:
            print(f"Código: {codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print()
            print("--------------------------------------------------")
        
    


## Ejemplo 2 de listar
def reporte_stock_bajo():
    cantidad =0
    while cantidad >= 0:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad >= 0:
                print("ingrese unnum mayor que 0")
            else:
                print("Error: La cantidad debe ser un número entero positivo o mayor que 0.")

        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
            cantidad = 0
    productos_bajo_stock = {}
    for codigo, producto in inventario.items():
        if producto["cantidad"] < cantidad:
            productos_bajo_stock[codigo] = producto
    if len(productos_bajo_stock) == 0:
        print ("No hay productos con stock bajo.")
    else:
        print("Productos con stock bajo:")
        mostrar_productos(productos_bajo_stock)
#################################################}


def buscar_productos_por_nombres():
    nombre = input("Ingrese el nombre del producto que desea buscar: ").lower()
    productos_encontrados = {}
    for codigo, producto in inventario.items():
        if nombre in producto["nombre"].lower():
            productos_encontrados[codigo] = producto
    if len(productos_encontrados) == 0:
        print("No se encontraron productos con ese nombre.")
    else:
        print("Productos encontrados:")
        mostrar_productos(productos_encontrados)

def eliminar_producto():
    mostrar_productos()
    codigo = int(input("Ingrese el código del producto que desea eliminar: "))
    if codigo in inventario:
        del inventario[codigo]
        print("Producto eliminado con éxito.")
    else:
        print("El producto no existe en el inventario.")
        print("--------------------------------------------------")
        print("--------------------------------------------------")

def menu():
    while True:
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar stock")
        print("4. Informe de productos")
        print("5. Reporte de productos con bajo stock")
        print("6. Buscar producto")
        print("7. Eliminar producto")
        print("8. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_stock()
        elif opcion == "4":
            informe_productos()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            buscar_producto()
        elif opcion == "7":
            eliminar_producto()
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu()

"""como guardar el diccionario inventario[] en una base de datos mysql"""
import mysql.connector
import json
mydb = mysql.connector.connect(
  host="localhost",
  user="XXXX",
  password="",
  database="XXXXXXXXXX"
)
mycursor = mydb.cursor()
sql = "INSERT INTO inventario (nombre, descripcion, cantidad, precio, categoria) VALUES (%s, %s, %s, %s, %s)"
for codigo, producto in inventario.items():
    val = (producto["nombre"], producto["descripcion"], producto["cantidad"], producto["precio"], producto["categoria"])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    

