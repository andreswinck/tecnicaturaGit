# Ejercicio 5: Tabla de multiplicar
# Hacer un programa que pida un número y guarde en una
# lista su tabla de multiplicar hasta el 10
tabla = []
num = int(input("Ingrese un número para dar la tabla de multiplicar del mismo: "))
for i in range(0,11):
    multiplo = num * i
    tabla.append(multiplo)
print(f"la tabla del {num} es: ")
print(tabla)
