# Ejercicio 1: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar
# la lista con en bucle for, Los elementos se deben mostrar
# de la siguiente forma:
# 1-2-3-4-5

# mi solución

# lista = []
# for i in range(0, 51):
#     lista.append(i)
#
# for i in range(0, 51):
#     print(f"{lista[i]}", end="-")

# la del profe

# lista = []
# i = 1
# while i <=50:
#     lista.append(i)
#     i +=1
lista = list(range(1, 51))  # algoritmo eficaz
for i in lista:
    print(i,end="-")
