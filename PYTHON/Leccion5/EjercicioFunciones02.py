#Ejercicio 2: Funcion con *args para multiplicar
#Crear una funcion para multiplicar los valores recibidos
#de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
#la multiplicación de todos los valores pasados como argumentos

# definimos la funcion para muiltuplicar

def multiplicar_valores(*args):  # El más utilizado es *args
    resultado = 1  # el cero no nos ayuda con la multiplicación
    for numero in args:
        resultado *= numero
    return resultado


# llamamos la función
print(multiplicar_valores(3, 5, 15, 3))  # le pasamos los argumentos
