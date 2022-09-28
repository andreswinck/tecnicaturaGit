# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numérico, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.


def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma


print(sumar_numeros(2, 3, 4, 5))
