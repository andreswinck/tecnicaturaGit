import math
#dada la siguiente tupla
tupla = (13,1,8,3,2,5,8)
#Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1,3,2]
lista=[] # definimos lista vacia
#filtramos elementos menores a 5
for num in tupla:
    if num < 5:
        lista.append(num)
print(lista)

# Ejercicio de matematica
# Para sacar la raiz cuadrada

numero = int(input("Digite un número positivo "))
while numero < 0:
    print("Error, debe ser un numero positivo ")
    numero = int(input("Digite un número positivo "))

print(f"\n Su raiz cuadrada es: {math.sqrt(numero):.2f}")
