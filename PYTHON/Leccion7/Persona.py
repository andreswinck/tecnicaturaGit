class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self): # Override = Sobreescribir
        return f"Persona: [ Nombre: {self._nombre}, Edad: {self.edad}]"


class Empleado(Persona):  # Hereda de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo


empleado1 = Empleado("Ariel", 40, 75000)

print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

# tarea: Encapsular los atributos y agregar los metodos getters and setters
# Crear otro objeto, pasar los datos para nomnbre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente