# Ejercicio1 : Eliminar duplicados de una lista
# Escribir un programa que tenga una lista y que a continuacion elimine
# los elementos repetidos. Por ultimo mostrar la lista

lista1 = [1, 1, 2, 2, 3, 3, 4, 4]
print(lista1)
#conjunto1 = set(lista1)
#print(conjunto1)
#lista1 = list(conjunto1)
#print(f"la lista quedó {lista1}")
lista1 = list(set(lista1))
print(lista1)





