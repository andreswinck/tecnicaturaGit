# dar formato a un string
nombre = 'Ariel'
edad = 28
mendaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
# print(mendaje_con_formato)
persona = ('Carla','Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s, tu saldo es de $%.2f pesos'  # % persona
# print(mensaje_con_formato % persona)
nombre = 'Juan'
edad = 19
sueldo = 3000
# mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'  .format(nombre, edad, sueldo)
# print(mensaje_con_formato)
# mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'  .format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'  .format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 59, 'sueldo': 7000}
mensaje = 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]}'.format(persona=diccionario)
print(mensaje)



