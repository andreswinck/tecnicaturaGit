from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creación de objeto clase Cuadrado".center(50, "_"))
cuadrado1 = Cuadrado(8,"azul")
cuadrado1._alto = 7
cuadrado1._ancho = 7
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# metodo MRO = Method Resolution Order
# print(Cuadrado.mro())

print(cuadrado1)
print("Creación del objeto clase Rectángulo".center(50,"_"))
rectangulo1 = Rectangulo(3,9,"verde")
rectangulo1._ancho = 8
print(f"Cálculo del área del rectángulo: {rectangulo1.calcular_area()}")
print(rectangulo1)

# figura1 = FiguraGeometrica() No se puede instanciar, es abstracta
print(Cuadrado.mro())

