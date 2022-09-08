# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los numeros del 1 al 10, luego modificar los
# elementos multiplicandolos por un numero ingresado por el usuario

# lista = []
# for i in range(1, 11):
#     lista.append(i)
# print(lista)
# factor = int(input("ingrese un numero: "))
#
# # for i in range(1, 11):
# #     lista[i] *= factor
#
# lista = lista * factor
#
# for i in range(1, 11):
#     print(f"{i} por {factor} = {lista[i]}")

lista = list(range(1,11))
print("lista original")
for i in lista:
    print(i, end="-")
valor = int(input("\nDigite un valor para multiplicar"))

for indice, i in enumerate(lista):
    lista[indice] *= valor
print(f"Lista final con los elementos multiplicado por {valor}")
a = 0
for i in lista:
    a += 1
    print(a, f"por {valor} ", i)

