"""funciones  se deben definir """
def saludar(nombre="invitado"):
    saludo ="Hola" + nombre
    return saludo
    #print(f"hola mundo {nombre}")


saludar("Mariano")

nombre = "Mariano"
saludar(nombre)

print (saludar(nombre))

def suma(a=0, b=0):
    return a + b   
print(suma(5, 3))

