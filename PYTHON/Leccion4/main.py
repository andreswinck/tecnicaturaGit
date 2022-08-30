# lista = Ariel. Liliana, Natalia, Osvaldo

nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0:2])  # no muestra el indice 2 (solo 2 elementos)
print(nombres[0:3])  # muestra 0,1 y 2
print(nombres[1:])  # desde el indicado hasta el final
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos")
print(len(nombres))

nombres.append("Marcelo")  # inserta el elemento en el último lugar
print(nombres)

nombres.insert(1, "Alberto")  # inserta un elemento en el índice que se especifica (indice,"elemento")
print(nombres)

nombres.insert(3, "Debora")
print(nombres)

nombres.remove("Alberto")  #eliminar un elemento
print(nombres)

nombres.pop()  #elimina el ultimo elemento por default
del nombres[2]  # elimina una posicion especifica

nombres.clear()
print(nombres)
del nombres  # elimina la lista NOMBRES

#  print(nombres)
# Definimos una TUPLA
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)  # IMPRIME LOS ELEMENTOS DE COCINA
print(len(cocina))  # IMPRIME LA LONGITUD DE LA TUPLA
print(cocina[0])  # imprime el primer elemento de la tupla
print(cocina[-1])  # imprime el ultimo elemento

# acceder a un rango

print(cocina[0:2])

# ejemplo

verduras = ("papa",)  # una tupla aunque sea de Un elemento necesita si o si la COMA!!!! sino es un STRING CADENA

# recorremos los elementos de la TUPLA
for cocinar in cocina:
    print(cocinar, end=" ")  # print usa el \n para recorrer las tuplas o listas con end=" " se ve todo ene una linea

cocinalista = list(cocina)  # convertimos la TUPLA en LISTA
cocinalista[0] = "plato"  # agrego el elemento
cocina = tuple(cocinalista)  # lo convierto en TUPLA de nuevo
print("\n", cocina)

# del cocina   asi se elimina una TUPLA













