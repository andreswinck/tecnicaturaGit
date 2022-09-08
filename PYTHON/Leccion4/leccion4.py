#lista = Ariel , Liliana , Natalia , Osvaldo
#COLECCIONES EN PYTHON

# Las listas se conocen en otros lenguajes como ARREGLOS O VECTORES

nombres =["Naty","Osvaldo","Lily","Ariel"]
print(nombres)
# print(nombres[0])
# print(nombres[1])
# print(nombres[3])
# print(nombres[-1])
# print(nombres[-2])
print(nombres[0:2]) # muestra los dos primeros
print(nombres[ :3]) # muestra todos menos el ultimo
print(nombres[1:])
#modificamos valores
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# cuantos elementos tiene la lista
print(len(nombres))

# Agregamos elemento
nombres.append("Marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
print(nombres)

# agregar elemento en indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

#Eliminar elementos
nombres.remove("Alberto")
print(nombres)

#Eliminar ultimo elemento
nombres.pop()
print(nombres)

#eliminar indice especifico

del nombres[2]
print(nombres)

#Eliminar todos los elementos
nombres.clear()
print(nombres)

#Eliminar lista

del nombres
# print(nombres)

# Definimos una tupla
cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))
# acceder a un elemento de la tupla con corchetes
print(cocina[0])
print(cocina[-1])
# acceder a un rango
print(cocina[0:2])
#ejemplo debe tener una coma por lo menos, sino es un string
verduras = ("papa",)

for cocinar in cocina:
    print(cocinar, end=" ") # imprime un elem. al lado del otro

cocinalista = list(cocina)

cocinalista[0]="plato"
cocina = tuple(cocinalista)
print("\n",cocina)

#del cocina esto es para borrar una tupla

# Tipo Set (o conjunto) 
#  guarda los elementos aleatoriamente sin INDICE 
planetas={"Marte","Jupiter","Venus"}
print(len(planetas))


# revisar si elemnto esta en el Set
print("Marte"in planetas)

#Agregar un elemento
planetas.add("Tierra") # add es una funcion
#No se pueden agregar elementos REPETIDOS
planetas.add("Tierra")
# SET se usa cuando no queremos que haya datos duplicados
print(planetas)

# Eliminar elementos
planetas.remove("Jupiter") # si tenemos algun error de tipeo, da error
print(planetas)
planetas.discard("Tierra") # Discard no presenta el error, pero no lo borra
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
del planetas
# print(planetas)

#DICCIONARIOS
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "POO": "Programación Orientada a Objetos",
    "SABD": "Sistema de Administración de Base de Datos"
}
print(len(diccionario))
print(diccionario)

#Acceder a un Diccionario a partir de las LLAVES
print(diccionario["IDE"])

#Otra forma con.GET
print(diccionario.get("POO"))

#Modificando elementos
diccionario["IDE"]="Entorno de desarrollo integrado"
print(diccionario)
print("las llaves")
# Como recorrer elementos
for termino in diccionario: # accedemos mostrando solo las llaves
    print(termino)
# con items() podemeos acceder a las laves y el valor
print(" items() muestra llave y valor")
for termino, valor in diccionario.items():
    print(termino, valor)

print("keys () muestra solo las llaves")
for termino in diccionario.keys():
    print(termino)
print("values() muestra solo los valores sin las llaves")
for valor in diccionario.values():
    print(valor)
# devuelve un boolean
print("existe IDE en el diccionario (T/F) = ", "IDE" in diccionario)

print("agregamos elemento")
diccionario["PK"] = "Llave Primaria"
print(diccionario)

print("eliminamos un elemento (SABD)")
diccionario.pop("SABD")
print(diccionario)

print("vaciamos diccionario")
diccionario.clear()
print(diccionario)

print("eliminar diccionario")
del diccionario
# print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3,1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # extend agrega varios elementos a una lista
print(lista3)

print(lista3.index(5)) #nos muestra en que posicion está el elemento indicado
# print(lista3.index(0)) genera error por no pertenecer el 0 a la lista

#como saber cuantos valores repetidos hay en una lista
print(lista3.count(1))

# poner al reves una lista
lista3.reverse()
print(lista3)

# multiplicar repitiendo elementos
print("multiplicamos una lista por dos (se repite 2 veces")
lista3 = lista3 * 2
print(lista3)

# métodos de ordenamiento .sort()

lista3.sort()
print(lista3)
# ordenamiento al REVES .sort(reverse=True)
lista3.sort(reverse=True)
print(lista3)

# Repaso de TUPLAS
tupla =(4, "Hola", 6.4, [1, 2, 78], 4, "Hola")
print(tupla)

print(4 in tupla)  # buscar elementos (T/F

#repaso de set o conjunto
# un conjunto o SET no puede tener elementos DUPLICADOS son valores UNICOS

conjunto2 = set()
conjunto1 = {"bye" }  #si se inicializa el conjunto con llaves debe terer al menos un valor
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
print("preguntamos si 3 está en conjunto1")
print(3 not in conjunto1)

# igualdad de dos conjuntos
print("preguntamos si los conjuntos son iguales")
print(conjunto1 == conjunto2)

# operaciones con conjuntos
print("union")
conjunto3 = conjunto1 | conjunto2 # une conjuntos
print(conjunto3)
print("interseccion")
conjunto3 = conjunto1 & conjunto2 # INTERSECCION DE CONJUNTOS
print(conjunto3)
print("resta conj1 - conj2 muestra bye")
conjunto3 = conjunto1 - conjunto2
print(conjunto3)
print("resta conj2 - conj1 muestra 7")
conjunto3 = conjunto2 - conjunto1
print(conjunto3)
print("elementos que no estan compartidos bye y 7")
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

print("preguntamos si C1 y C2 es SUBCONJUNTO de C3")
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))
print(conjunto2.issubset(conjunto3))
# seguir con video 2s12

print("preguntamos si C3 es SUBCONJUNTO de C1 y C2")
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print("preguntamos si C3 contiene a C1 y C2 o sea un SUPERCONJUNTO")
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print("preguntamos si C2 es SUPERCONJ. de C3")
print(conjunto2.issuperset(conjunto3))
print("como saber si son DISCONEXOS o sea no comparten ningun elemento")
print(conjunto1.isdisjoint(conjunto2))
print("convertir conjunto en INMUTABLE con Frozenset")
conjunto1 = frozenset

diccionarionuevo = {"Azul":"Blue", "Rojo":"Red", "Verde":"Green" , "Amarillo":"Yellow"}
print(diccionarionuevo)
del diccionarionuevo["Azul"]
print(diccionarionuevo)

diccionario2 = {"Ariel": {"Edad": "40", "Altura":"1.83"}, "Osvaldo": [45, 1.85], "Natalia": [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 millones", "Posición": "Extremo Derecho"},
    11: {"Nombre": "Ángel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 millones", "Posición": "Extremo Derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 millones", "Posición": "Media Punta"},
    19: {"Nombre": "Nicolas Otamendi", "Edad": 28, "Altura": 1.83, "Precio": "3.5 millones", "Posición": "Defensa Central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 millones", "Posición": "Arquero"},
    7: {"Nombre": "Rodrigo de Paul", "Edad": 28, "Altura": 1.80, "Precio": "25 millones", "Posición": "Centrocampista"},
    3: {"Nombre": "Nicolas Tagliafico", "Edad": 30, "Altura": 1.7, "Precio": "11 millones", "Posición": "Defensa"},
    8: {"Nombre": "Marcos Acuña", "Edad": 30, "Altura": 1.72, "Precio": "11 millones", "Posición": "Lateral Derecho"},
    5: {"Nombre": "Leandro Paredes", "Edad": 28, "Altura": 1.80, "Precio": "13 millones", "Posición": "Centrocampista"},
}
# print(seleccionArgentina.values())
for llave, valor in seleccionArgentina.items():
    print(llave,valor)
print("Tenemos cargados la cantidad de:", end=" ")
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

#Agregamos elementos a la pila (se agregan al final)
pila.append(4)
pila.append(5)
print(pila)

# sacamos elementos de la pila
elementoBorrado = pila.pop()
print(f" Sacamos el elemento {elementoBorrado}")
print(f"La pila ahora quedó así {pila}")

# Colas con Listas
# estructura tipo FIFO first in first out
cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]
# agregamos elemento al final
cola.append("Natalia")
cola.append("José")
print(cola)

# sacamos elementos
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)


