"""Ejercicio 5 Sistema de calificaciones
Le pedimos al usuario que ingerse un valor del 0 al 10
Si ingreso 9 o 10 imprimimos A
Si ingreso 8 y menor que 9 imprimimos B
Si ingreso 7 y menor que 8 imprimimos C
Si ingreso 6 y menor que 7 imprimimos D
Si ingreso 0 y menor que 6 imprimimos F
de lo contrario valor incorrecto
"""
nota = float(input("Digite la nota entre 0 y 10: "))
if 0 <= nota < 6:
    print("la nota es F")
elif 6 <= nota < 7:
    print("la nota es D")
elif 7 <= nota < 8:
    print("la nota es C")
elif 8 <= nota < 9:
    print("la nota es B")
elif 9 <= nota < 10:
    print("la nota es A")
else:
    print("Valor incorrecto")

