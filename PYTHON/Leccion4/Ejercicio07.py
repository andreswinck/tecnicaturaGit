# Ejercicio 7: Juego adivina un número
# Realiza un juego para adivinar un número
import random
numero = int(input("Adivine el número entre 0 y 100: "))
aleatorio = random.randint(0, 100)
conteo = 0
while numero >= 0:
    conteo += 1
    if numero < aleatorio:
        numero = int(input("El número que buscas es mayor al ingresado: "))
    elif numero > aleatorio:
        numero = int(input("El número que buscas es menor al ingresado: "))
    else:
        print(f"Felicidades! adivinaste el número en --> {conteo} <-- intentos")
        break
