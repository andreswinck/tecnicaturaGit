# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados Celsius
# a fahrenheit y viceversa.
# Investigar fórmulas
# celsius = (far-32)/1.8
# fahrenheit = (cel*1.8) + 32

def conversion_fahrenheit(grados):
    far = (grados * 1.8) + 32
    return far


def conversion_celsius(grados):
    cel = (grados-32)/1.8
    return cel


temperatura = float(input("Ingrese la temperatura en ºC: "))
print(f"La temperatura en ºF es de: {conversion_fahrenheit(temperatura):.2f}")

temperatura = float(input("Ingrese la temperatura en ºF: "))
print(f"La temperatura en ºC es de: {conversion_celsius(temperatura):.2f}")









