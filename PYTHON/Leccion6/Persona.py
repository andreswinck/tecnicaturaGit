class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama método INIT Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  # self es igual a This de Java
        print(f"La clase Persona tiene los siguientes datos (mostrar detalle): "
              f"{self.nombre}, "
              f" {self.apellido}, "
              f"{self._dni}"
              f"{self.edad}, "
              f"la direccion es: {self.args},"
              f"los datos importantes son: {self.kwargs}")


persona1 = Persona("Ariel", "Betancud", 32456987, 40)  # necesitamos arguumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
persona2 = Persona("Osvaldo", "Giordanini",302323, 45)
print(f"El objeto1 de la clase tiene "
      f"por nombre: "
      f"{persona1.nombre} "
      f"por apellido: "
      f"{persona1.apellido} "
      f"y la edad es: "
      f"{persona1.edad}")
print(f"El objeto2 de la clase persona: "
      f"{persona2.nombre} "
      f"{persona2.apellido} "
      f"{persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido ="Buccela"
persona1.edad = 40

print(f"El objeto1 MODIFICADO de la clase tiene "
      f"por nombre: "
      f"{persona1.nombre} "
      f"por apellido: "
      f"{persona1.apellido} "
      f"y la edad es: "
      f"{persona1.edad}")

# Los atributos son caracteristicas que van a tener los objetos
# Los metodos son EL COMPORTAMIENTO que va a tener el objeto
persona1.mostrar_detalle() # la referencia se pasa de forma automática
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # debemos pararle una referencia para el self o dará error
persona1.telefono = "4444555321"
print(f"Este es el teléfono de {persona1.nombre}:  {persona1.telefono}")  # hemos creado un atributo de un objeto
# print(persona2.telefono) el objeto persona2 no tiene el atributo telefono solo es de persona1
persona3 = Persona("Rogelio", "Romero",35212124, 22, "teléfono", "26123546546", "Carlos Lopez", 823, "Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorito="Azul", Auto="Citroen", Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) # esto no se puede utilizar en python porque está PROTEGIDO (encapuslado) COMO SUGERENCIA
# persona3.__nombre # Está totalmente encapsulado


