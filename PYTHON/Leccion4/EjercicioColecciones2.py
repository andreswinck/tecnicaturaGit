# Ejercicio2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no debe haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista1 = ["a", "c", "d", "e", "g"]
lista2 = ["b", "c", "e", "f"]
conj1 = set(lista1)
conj2 = set(lista2)
print(f"Lista de palabras que aparecen en las listas {list(conj1 | conj2)}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda {list(conj1-conj2)}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera {list(conj2-conj1)}")
print(f"Lista de palabras que aparecen en ambas listas {list(conj1 & conj2)}")



