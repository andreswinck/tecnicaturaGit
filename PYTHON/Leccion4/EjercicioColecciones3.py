# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase : Guerrero
# Raza : Dunadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Elfo Sindar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []
# creamos diccionarios
p = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dunadan del norte"}
personajes.append(p)
p = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Elfo Sindar"}
personajes.append(p)
p = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(p)
p = {"Nombre": "Gollum", "Clase": "Fuertes", "Raza": "Hobbit"}
personajes.append(p)

for i in personajes:
    print(f"{i} -> {personajes[i]}")

