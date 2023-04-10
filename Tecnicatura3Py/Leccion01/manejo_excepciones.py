from NumerosIgualesException import NumerosIgualesException

resultado = None
a = 7
b = 0
try:
    a = int(input("digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    if a==b:
        raise NumerosIgualesException("Son numeros iguales")
    resultado = a/b # modificamos
except TypeError as e:
    print(f"Type error - Ocurrió un error: {type(e)}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError - Ocurrió un error: {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrió un error: {type(e)}")
else:
    print("No se arrojo ninguna excepcion")
finally: # Siempre se va a ejecutar
    print("Ejecucion del bloque final")
print(f"El resultado es: {resultado}")
print("Seguimos...")
