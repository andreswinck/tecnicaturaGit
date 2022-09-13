# Ejercicio 5: Calcular el factorial de un número
factorial = 1
numero = int(input("Ingrese el número para calcular el factorial: "))
while numero<0:
    print("El número es negativo ingrese un número positivo")
    numero = int(input("Ingrese el número para calcular el factorial: "))
for i in range(1,numero+1):
    factorial *= i
print(f"El factorial de {numero}, es {factorial}")
