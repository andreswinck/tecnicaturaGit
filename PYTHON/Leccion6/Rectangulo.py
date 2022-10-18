class Rectangulo:
    """
    Crear una clase llamada rectangulo que debe tener 2 atributos: altura y base
    el nombre del metodo será clacular area utilizando la formula
    area = base x altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    # Metodo de cálculo de area

    def calcular_area(self):
        return self.base * self.altura


base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la base del rectángulo: "))
rectangulo1 = Rectangulo(base, altura)
print(f"El área del rectángulo es: {rectangulo1.calcular_area()}")

