class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property  # decorador
    def nombre(self):  # metodo getter
        print("Estamos usando el metodo GET")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # metodo Setter
        print("Estamos usando el metodo SET")
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # metodo getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido): # metodo Setter
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # metodo getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # metodo Setter
        self._edad = edad


persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.nombre)  # Llamamos al metodo GETTER
persona1.nombre = "Juan Pedro"  # llamamos al metodo Setter
print(persona1.nombre)  #llamamos al metodo Getter
print(persona1.mostrar_detalle())  # llamamos al metodo mostrar detalles
print(persona1.edad)
# Crear tres objetos mas con getter y setter
# modificarlos y mostrar los cambios con mostrar detalles
#persona2
print("Persona2")
persona2 = Persona2("Dante", "Martinez", 48)
print(persona2.nombre, persona2.apellido, persona2.edad)
persona2.nombre = "Nicolas"
persona2.apellido = "Martin"
persona2.edad = 47
print(persona2.mostrar_detalle())
#persona3
persona3 = Persona2("Abel", "Pierna", 18)
print("Persona3")
print(persona3.nombre, persona3.apellido, persona3.edad)
persona3.nombre = "Cain"
persona3.apellido = "Brazo"
persona3.edad = 19
print(persona3.mostrar_detalle())
#persona4
print("Persona4")
persona4 = Persona2("Natalia", "Gimenez", 38)
print(persona4.nombre, persona4.apellido, persona4.edad)
persona4.nombre = "Carina"
persona4.apellido = "Carranza"
persona4.edad = 29
print(persona4.mostrar_detalle())
