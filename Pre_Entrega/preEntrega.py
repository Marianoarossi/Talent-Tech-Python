"""Crear un menú interactivo utilizando bucles while y condicionales if-elif-else y lista:
● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos.
● Entre las opciones, deben incluirse: agregar productos al productos y mostrar los productos registrados.
Teniendo en cuenta esto 
Implementar la funcionalidad para agregar productos a una lista:
● Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada

Mostrar los productos ingresados:
● Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el
momento."""


# Inicializar la lista de  productos como una lista vacía
productos = []
print("\n ############################################################\n")
print("\tBienvenido al programa de gestión de productos.")
print("\n ############################################################\n")

while True: #Ingresa al menú

    print("\nIngrese una opción del menú:\n\t1. Agregar producto al inventario\n\t2. Consultar de un producto\n\t3. Modificar la cantidad de un producto\n\t4. Eliminar un producto del inventario\n\t5. Listar productos registrados\n\t6. Listar productos con stock bajo\n\t7. Salir")

    opcion = input("Seleccione una opción: \n") #toma la opción ingresada por el usuario.
    
    if opcion == "1":# Si la opción es 1 ingresa a la condición para solicitar el nombre del producto
        # llamada a la funcion AgregarProducto()
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
        else:
            producto = [nombre, cantidad]
            productos.append(producto)
            print("Producto agregado al productos.")

    elif opcion == "2": # Consultar un producto
        #Llamada a la función ConsultarProducto()
        nombre = input("Ingrese el nombre del producto a consultar: ")
        encontrado = False 
        for producto in productos:
            if producto[0] == nombre:
                print(f"Producto: {producto[0]}, Cantidad en stock: {producto[1]}")
                encontrado = True
                break
        if not encontrado: # se consulta  la variable encontrado, si esta en False imprime no encontrado 
            print("No se encontró el producto.")

    elif opcion == "3": # Modificar la cantidad de un producto 
        #Llamada a la función ModificarCantidad()
        nombre = input("Ingrese el nombre del producto a modificar: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        if nueva_cantidad <= 0: #validamos que la cantidad sea superior a 0
            print("La cantidad debe ser mayor a 0.")
        else:
            for producto in productos:
                if producto[0] == nombre:
                    producto[1] = nueva_cantidad
                    print(f"La cantidad del producto '{nombre}' fúe actualizada a {nueva_cantidad}.")
                    break
            else:
                print("Producto no encontrado.")

    elif opcion == "4":  # Eliminar un producto del inventario
        #Llamada a la función EliminarProducto()
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        for producto in productos:
            if producto[0] == nombre:
                productos.remove(producto)
                print(f"El producto '{nombre}' fue eliminado del inventario.")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró el producto.")

    elif opcion == "5":
        if len(productos) == 0:
            print("No hay productos registrados en el Inventario.")
        else:
            print("Productos registrados en el Inventario:")
            i = 0
            while i < len(productos):
                producto = productos[i]
                print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}")
                i += 1


    elif opcion == "6":  #opcion para listar los productos de bajo stock dependiendo la cantidad definida por el usuario.
        #Llamada a la función ListarStockBajo()
        cantidad_limite = int(input("Ingrese la cantidad límite: "))
        productos_bajo_stock = []
        
        for producto in productos:
            if producto[1] <= cantidad_limite:
                productos_bajo_stock.append(producto)
        
        if productos_bajo_stock:
            print("Productos con stock bajo:")
            for producto in productos_bajo_stock:
                print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}")
        else:
            print("No hay productos con stock bajo.")


    elif opcion == "7":
        print("Finalizó la sesión del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
