"""uso de try y except"""
while True:
    try:
        numero = int(input("ingrese un numero: "))
        print(5/numero)
        break
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    except ValueError:
        print("debe ingresar un numero")
    except:
        print("algo salio mal")


def pedirnroentero():
    while True:
        try:
            numero = int(input("ingrese un numero: "))
            return numero
        except ValueError as e: 
            print("El error es: ", e)
        
numero = pedirnroentero()
print(numero)
