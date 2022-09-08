# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir numeros y meterlos en lista
# cdo el usuario ponga 0 salir
# Ordenar los num de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input("Digite un numero (0 para salir): "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()  # la lista esta ordenada
print(f"\n lista ordenada\n{lista}")
