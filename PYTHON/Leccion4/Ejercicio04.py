# Ejercicio 4: Hacer un programa para sumar números pares dentro de un rango
# HAcer un programa para sumar números pares dentro
# de un rango

inicio = int(input("Ingrese el número de inicio del rango: "))
final = int(input("Ingrese el número final del rango: "))
suma = 0
for i in range(inicio, final+1):
    if i % 2 == 0:
        suma += i
    else:
        continue
print(f"La suma de los números pares entre {inicio}, y {final}, es: {suma}")


