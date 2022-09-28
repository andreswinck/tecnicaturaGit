# Ejercicio 11: Agenda Telefónica
# Hacer un programa que simule una agenda de contactos: Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir

agenda = {}
while True:
    print("\t.:Menú:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Ingrese la opcion de menú: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el número de teléfono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente")
        else:
            print("El contacto ya existe")
    elif opcion == 2:
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Contacto eliminado exitosamente")
        else:
            print("Éste contacto no existe en la agenda")
    elif opcion == 3:
        print("AGENDA DE CONTACTOS")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, teléfono {valor}")
    elif opcion == 4:
        print("Gracias por utilizar la agenda")
        break
    else:
        print("Se equivocó de opción")
    print()

