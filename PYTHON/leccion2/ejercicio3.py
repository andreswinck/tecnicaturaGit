"""Ejercicio3
Pedir al usuaroi que ingrese un mes del año, entre 1 y 12
y le decimos en que estación del año estamos
1-3 verano
4-6 otoño
7-9 invierno
10 - 12 primavera"""

mes = int(input("Digite el mes del año para decirle en que estación está: (1 al 12) "))
if 1 <= mes <= 3:
    print(f"el mes {mes} pertenece a la estación VERANO")
elif 4 <= mes <= 6:
    print(f"el mes {mes} pertenece a la estación OTOÑO")
elif 7 <= mes <= 9:
    print(f"el mes {mes} pertenece a la estación INVIERNO")
elif 10 <= mes <= 12:
    print(f"el mes {mes} pertenece a la estación PRIMAVERA")
else:
    print("Usted ingresó una opción incorrecta")


