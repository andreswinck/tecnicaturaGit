from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5,"azul")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# metodo MRO = Method Resolution Order

print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(4,5,"verde")
print(f"Cálculo del área del rectángulo: {rectangulo1.calcular_area()}")
print(rectangulo1)
